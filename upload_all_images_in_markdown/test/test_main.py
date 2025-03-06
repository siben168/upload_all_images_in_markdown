"""
This module contains tests for the upload_all_images_in_markdown package.
It includes fixtures and test cases to verify the functionality of uploading images in markdown files.
"""

import os
import json
import pytest
from PIL import Image
from upload_all_images_in_markdown.main import main

# Load configuration from config.json
with open('config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)


@pytest.fixture(scope="module")
def setup_test_vault():
    """
    Fixture to set up a test vault directory with sample markdown files and images.

    Yields:
        tuple: A tuple containing the test vault directory path, upload URL, cleanup flag,
        and sample markdown file path.
    """
    test_vault_dir = config['test_vault_dir']
    upload_url = config['test_upload_url']
    cleanup = False

    # Setup test vault directory
    if not os.path.exists(test_vault_dir):
        os.makedirs(test_vault_dir)

    # Create a sample markdown file with image links
    sample_md_file = os.path.join(test_vault_dir, 'sample.md')
    with open(sample_md_file, 'w', encoding='utf-8') as f:
        f.write('![Image](image1.png)\n')
        f.write('![Image](image2.png)\n')

    # Create sample images
    sample_image1 = os.path.join(test_vault_dir, 'image1.png')
    sample_image2 = os.path.join(test_vault_dir, 'image2.png')

    # Generate simple images using PIL
    image1 = Image.new('RGB', (100, 100), color='red')
    image1.save(sample_image1)
    image2 = Image.new('RGB', (100, 100), color='blue')
    image2.save(sample_image2)

    yield test_vault_dir, upload_url, cleanup, sample_md_file

    # Clean up sample markdown file and images
    if os.path.exists(sample_md_file):
        os.remove(sample_md_file)
    if os.path.exists(sample_image1):
        os.remove(sample_image1)
    if os.path.exists(sample_image2):
        os.remove(sample_image2)


def test_upload_images_with_cleanup(setup_test_vault):  # pylint: disable=redefined-outer-name
    """
    Test case to verify the image upload functionality with cleanup.

    Args:
        setup_vault_fixture (tuple): A tuple containing the test vault directory path,
        upload URL, cleanup flag, and sample markdown file path.
    """
    test_vault_dir, upload_url, cleanup, sample_md_file = setup_test_vault
    cleanup = True  # Enable cleanup
    main(test_vault_dir, upload_url, cleanup)

    # Check if the markdown file has been updated with new URLs
    with open(sample_md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        assert '![Image](image1.png)' not in content
        assert '![Image](image2.png)' not in content
        assert config['base_url'] in content

    # Check if the images have been deleted
    sample_image1 = os.path.join(test_vault_dir, 'image1.png')
    sample_image2 = os.path.join(test_vault_dir, 'image2.png')
    assert not os.path.exists(sample_image1)
    assert not os.path.exists(sample_image2)
