<div align="center">
<h1 align="center">upload-all-images-in-markdown</h1>

简体中文 / [English](#english-documentation)

将文件夹中所有 Markdown 文件内的图片链接转换为在线 Markdown 链接，并通过 PicList/PicGo 服务上传。

Convert image links in all Markdown files within a folder to online Markdown links and upload them via PicList/PicGo service.
</div>

### 目录

- [简介](#简介)
- [安装](#安装)
- [使用](#使用)
  - [使用命令行参数](#使用命令行参数)
  - [使用配置文件](#使用配置文件)
  - [结合使用](#结合使用)
- [配置](#配置)
- [运行测试](#运行测试)

### 简介

将本地图片链接转换为在线 Markdown 链接，并通过 PicList/PicGo 服务上传。

主要功能：
- 同时可选择清理本地图片。
- 支持配置文件，方便使用。
- 图片上传需要使用 PicList/PicGo 服务，建议使用[PicList](https://github.com/Kuingsmile/PicList)，需要先安装 [PicList](https://github.com/Kuingsmile/PicList) 并配置好图床。

### 出发点

想把有道云笔记里的几千篇笔记迁移到 Obsidian 中，感谢[youdaonote-pull](https://github.com/DeppWang/youdaonote-pull)提供的有道云笔记的全量导出功能，很快把所有笔记导出到了本地文件夹，但是由于几千张笔记中的图片也保留在本地，不方便移动端使用，所以想把图片上传到图床，使用markdown链接到笔记里。于是自己写了个批量转换并上传图片的程序。

### 安装

```bash
poetry install
```

### 使用

你可以通过命令行参数运行脚本，或者指定配置文件。

#### 使用命令行参数

```bash
poetry run upload-all-images-in-markdown <vault_directory> --upload_url <UPLOAD_URL> --cleanup
```

#### 使用配置文件

```bash
poetry run upload-all-images-in-markdown --config config.json
```

#### 结合使用

命令行参数会覆盖配置文件中的值。

```bash
poetry run upload-all-images-in-markdown --config config.json --upload_url <UPLOAD_URL>
```

### 配置

在运行测试之前，请在项目根目录下编辑 `config.json` 文件以包含您的具体配置值。您可以使用提供的 `config.sample.json` 作为模板：

- **vault_directory**: 这是包含您的 Markdown 文件的目录路径。

- **base_url**: 这是用于markdown链接的图床URL。将 `https://example.com/` 替换为您自己的图床 URL。

- **upload_url**: 这是处理图片上传的 PicList/PicGo 服务的 URL。将 `http://127.0.0.1:36677/upload` 替换为您的上传服务的实际 URL。

- **cleanup**: 用于确定图片上传后是否删除本地图片。如果您希望清理本地图片，请设置为 `true`；如果希望保留，请设置为 `false`。

- **test_vault_dir**: 这是用于测试目的的目录路径，仅供单元测试使用。

- **test_upload_url**: 这是用于测试上传功能的 URL。仅供单元测试使用。

### 运行测试

要运行单元测试，请使用以下命令：

```bash
poetry run pytest
```

---

## English Documentation

### Table of Contents

- [English Documentation](#english-documentation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Motivation](#motivation)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Using Command-Line Arguments](#using-command-line-arguments)
    - [Using a Configuration File](#using-a-configuration-file)
    - [Combining Both](#combining-both)
  - [Configuration](#configuration)
  - [Running Tests](#running-tests)

### Introduction

Convert image links in all Markdown files within a folder to online Markdown links and upload them via PicList/PicGo service.

Main features:
- Optionally clean up local images.
- Supports configuration files for ease of use.
- Image uploads require the use of PicList/PicGo services. It is recommended to use [PicList](https://github.com/Kuingsmile/PicList). You need to install [PicList](https://github.com/Kuingsmile/PicList) and configure the image hosting service.

### Motivation

I wanted to migrate thousands of notes from Youdao Cloud Notes to Obsidian. Thanks to [youdaonote-pull](https://github.com/DeppWang/youdaonote-pull) for providing a full export feature for Youdao Cloud Notes, I quickly exported all notes to a local folder. However, since the images in the thousands of notes were also kept locally, it was inconvenient for mobile use. Therefore, I wanted to upload the images to an image hosting service and use markdown links in the notes. So, I wrote a program to batch convert and upload images.

### Installation

```bash
poetry install
```

### Usage

You can run the script with command-line arguments or specify a configuration file.

#### Using Command-Line Arguments

```bash
poetry run upload-all-images-in-markdown <vault_directory> --upload_url <UPLOAD_URL> --cleanup
```

#### Using a Configuration File

```bash
poetry run upload-all-images-in-markdown --config config.json
```

#### Combining Both

Command-line arguments will override the values in the configuration file.

```bash
poetry run upload-all-images-in-markdown --config config.json --upload_url <UPLOAD_URL>
```

### Configuration

Before running the tests, edit a `config.json` file in the project root directory to include your specific configuration values. You can use the provided `config.sample.json` as a template:

- **vault_directory**: This is the path to the directory containing your Markdown files.

- **base_url**: This is the URL for the image hosting service used in markdown links. Replace `https://example.com/` with your own image hosting URL.

- **upload_url**: This is the URL of the PicList/PicGo service that will handle the image uploads. Replace `http://127.0.0.1:36677/upload` with the actual URL of your upload service.

- **cleanup**: Determines whether local images should be deleted after they are uploaded. Set it to `true` if you want to clean up local images, or `false` to keep them.

- **test_vault_dir**: This is the path to a directory used for testing purposes, intended for unit tests only.

- **test_upload_url**: This is the URL used for testing the upload functionality, intended for unit tests only.

Ensure that all paths and URLs are correctly set according to your environment and requirements. This configuration file is crucial for the script to function correctly, as it dictates where to find the Markdown files, where to upload the images, and how to handle the images post-upload.

### Running Tests

To run the unit tests, use the following command:

```bash
poetry run pytest
```
