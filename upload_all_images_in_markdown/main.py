"""
This script processes markdown files in a specified directory to upload local images to a given URL.
It replaces the local image paths in the markdown files with the URLs of the uploaded images.
Optionally, it can delete the local images after uploading.

Usage:
    python main.py <vault_directory> [--upload_url <upload_url>] [--cleanup] [--config <config.json>]

Arguments:
    vault_directory: Path to the Obsidian vault directory containing markdown files.
    --upload_url: URL of the upload API (default: http://127.0.0.1:36677/upload).
    --cleanup: Delete local images after upload.
    --config: Path to config.json file.
"""

import os
import re
import argparse
import json
import logging
import time
import urllib.parse
import requests


# Ensure the package is initialized
import upload_all_images_in_markdown  # noqa: F401, pylint: disable=unused-import


def upload_image(image_path, upload_url):
    """
    Uploads an image to the specified URL.

    Args:
        image_path (str): The path to the image file.
        upload_url (str): The URL to upload the image to.

    Returns:
        str: The URL of the uploaded image.
    """
    retries = 3
    for attempt in range(retries):
        try:
            response = requests.post(
                upload_url, json={'list': [image_path]}, timeout=10)
            response.raise_for_status()
            result = response.json()
            if result['success']:
                return result['result'][0]
            else:
                raise Exception("Image upload failed")
        except Exception as e:
            if attempt < retries - 1:
                wait_time = 2 ** attempt
                logging.warning(f"Upload failed, retrying in {
                                wait_time} seconds...")
                time.sleep(wait_time)
            else:
                logging.error("Upload failed after multiple attempts.")
                raise e


def process_markdown_file(file_path, upload_url, cleanup):
    """
    Processes a markdown file to upload local images and replace their paths with URLs.

    Args:
        file_path (str): The path to the markdown file.
        upload_url (str): The URL to upload images to.
        cleanup (bool): Whether to delete local images after uploading.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    image_paths = re.findall(r'!\[.*?\]\((?!http)(.*?)\)', content)
    processed_images = 0
    for image_path in image_paths:
        # Decode URL-encoded characters in the image path
        decoded_image_path = urllib.parse.unquote(image_path)
        if os.path.isabs(decoded_image_path):
            continue
        full_image_path = os.path.join(
            os.path.dirname(file_path), decoded_image_path)
        if os.path.exists(full_image_path):
            new_url = upload_image(full_image_path, upload_url)
            content = content.replace(image_path, new_url)
            logging.info(f"Uploaded image: {full_image_path} to {new_url}")
            if cleanup:
                os.remove(full_image_path)
                logging.info(f"Deleted local image: {full_image_path}")
            processed_images += 1

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

    logging.info(f"Processed file: {file_path} with {processed_images} images")
    return processed_images


def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def main(vault_directory, upload_url, cleanup):
    """
    Main function to process all markdown files in a given directory.

    Args:
        vault_directory (str): The path to the directory containing markdown files.
        upload_url (str): The URL to which images will be uploaded.
        cleanup (bool): Flag indicating whether to delete local images after upload.

    Raises:
        FileNotFoundError: If the specified vault_directory does not exist.
    """
    if not os.path.exists(vault_directory):
        raise FileNotFoundError(
            f"The directory {vault_directory} does not exist.")

    total_images = 0
    for root, _, files in os.walk(vault_directory):
        for file in files:
            if file.endswith('.md'):
                total_images += process_markdown_file(os.path.join(
                    root, file), upload_url, cleanup)

    logging.info(f"Total images processed: {total_images}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Upload all images in markdown files.")
    parser.add_argument('--vault_directory', type=str,
                        help='Path to the Obsidian vault directory')
    parser.add_argument('--upload_url', type=str,
                        help='URL of the upload API')
    parser.add_argument('--cleanup', action='store_true',
                        help='Delete local images after upload')
    parser.add_argument('--config', type=str, nargs='?', const='config.json', default='config.json',
                        help='Path to config.json file (default: config.json)')
    args = parser.parse_args()

    config = {}
    if args.config:
        config = load_config(args.config)

    vault_directory = args.vault_directory or config.get('vault_directory')
    if not vault_directory:
        parser.error("the following arguments are required: vault_directory")

    upload_url = args.upload_url or config.get(
        'upload_url', "http://127.0.0.1:36677/upload")
    cleanup = args.cleanup or config.get('cleanup', False)

    main(vault_directory, upload_url, cleanup)
