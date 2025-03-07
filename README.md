<div align="center">
<h1 align="center">upload-all-images-in-markdown</h1>

简体中文 / [English](#english-documentation)

将文件夹中所有 Markdown 文件内的图片链接转换为在线 Markdown 链接，并通过 PicList/PicGo 服务上传。

Convert image links in all Markdown files within a folder to online Markdown links and upload them via PicList/PicGo service.
</div>

### 目录

- [简介](#简介)
- [使用安装包运行程序](#使用安装包运行程序)
- [使用Python运行或开发](#使用Python运行或开发)
  - [安装](#安装)
  - [使用](#使用)
  - [配置](#配置)
  - [运行测试](#运行测试)

### 简介

将本地图片链接转换为在线 Markdown 链接，并通过 PicList/PicGo 服务上传。

主要功能：
- 自动扫描 Markdown 文件中的本地图片
- 支持批量上传到配置的图床
- 生成替换后的 Markdown 文件
- 可选择是否清理本地图片。
- 支持配置文件，方便使用。
- 图片上传需要使用 PicList/PicGo 服务，建议使用[PicList](https://github.com/Kuingsmile/PicList)，需要先安装 [PicList](https://github.com/Kuingsmile/PicList) 并配置好图床。

### 出发点

前段时间把有道云笔记里的几千篇笔记迁移到了 Obsidian 中，感谢[youdaonote-pull](https://github.com/DeppWang/youdaonote-pull)提供的有道云笔记的全量导出功能，很快把所有笔记导出到了本地文件夹，但是由于几千张笔记中的图片也保留在本地，笔记文件夹容量过大，也不方便多端同步和移动端使用，所以想把图片上传到图床，再使用markdown链接到笔记里。于是自己写了个批量转换并上传图片的程序。

## 使用安装包运行程序

下载windows或macOS的安装包，解压后配置`config.json`文件，运行程序即可。

1. 下载安装包
    - [🖥️ Windows 安装包](https://github.com/siben168/upload_all_images_in_markdown/releases/download/v0.1.0/upload-images-windows.zip)
    - [🍏 Mac OS 安装包](https://github.com/siben168/upload_all_images_in_markdown/releases/download/v0.1.0/upload-images-mac.zip)
2. 解压
3. 配置 `config.json` 文件
    - 配置 `vault_directory` 为笔记所在的文件夹路径
    - 配置 `upload_url` 为 PicList/PicGo 服务的 URL
    - 配置 `base_url` 为图床的 URL
    - 配置 `cleanup` 为是否清理本地图片
4. 运行        
    - Windows 用户双击 `upload-images.exe` 运行。
    - macOS 在terminal中输入 `./upload-images` 运行。

### 问题解决

 1. Mac版本出现`Apple无法验证“upload-images”是否包含可能危害Mac安全或泄漏隐私的恶意软件。`
    - 在 Mac 上，选取苹果菜单  >“系统设置”，然后点按边栏中的“隐私与安全性” 。（你可能需要向下滚动。）
    - 前往“安全性”，找到“已阻止upload-images***”选项。
    - 点按“仍然允许”。
    - 再次运行程序，在出现的对话框中选 “仍要打开”。
    - 使用密码验证。
    - 在弹出的对话框中选择 “允许访问” 文件夹（访问本地图片需要权限）。
    
## 使用Python运行或开发

如果安装包不满足需求，可以使用Python运行或开发。
### 安装

环境准备：python、poetry

直接运行poetry install即可完成依赖项和环境安装

```bash
poetry install
```

### 使用

你可以通过命令行参数运行脚本，或者指定配置文件。

#### 使用命令行参数

```bash
python upload_all_images_in_markdown/main.py <vault_directory> --upload_url <UPLOAD_URL> --cleanup
```

#### 使用配置文件

```bash
python upload_all_images_in_markdown/main.py --config config.json
```

不指定配置文件名时，会使用默认配置文件名`config.json`

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

- [Introduction](#introduction)
- [Motivation](#motivation)
- [Installation by Executable Package](#installation-by-executable-package)
- [Using Python for Running or Development](#using-python-for-running-or-development)
  - [Installation](#installation)
  - [Usage](#usage)
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

## Installation by Executable Package

Download the installation package for Windows or macOS, unzip it, and configure the `config.json` file. Then run the program.
1. Download the installation package
2. Extract it
3. Configure the `config.json` file
    - Set `vault_directory` to the path of your notes folder
    - Set `upload_url` to the URL of your PicList/PicGo service
    - Set `base_url` to the URL of your image hosting service
    - Set `cleanup` to determine whether to clean up local images
4. Run the program
    - Windows users can double-click `upload-images.exe` to run it.
    - macOS users can run `./upload-images` in the terminal.

### Using Python for Running or Development

If the executable package does not meet your needs, you can use Python to run or develop.

#### Installation

Prerequisites: Python, Poetry

Run the following command to install dependencies and set up the environment:

```bash
poetry install
```

#### Usage

You can run the script with command-line arguments or specify a configuration file.

##### Using Command-Line Arguments

```bash
python upload_all_images_in_markdown/main.py <vault_directory> --upload_url <UPLOAD_URL> --cleanup
```

##### Using a Configuration File

```bash
python upload_all_images_in_markdown/main.py --config config.json
```

If no configuration file is specified, the default `config.json` will be used.

##### Combining Both

Command-line arguments will override the values in the configuration file.

```bash
python upload_all_images_in_markdown/main.py --config config.json --upload_url <UPLOAD_URL>
```

#### Configuration

Before running the tests, edit a `config.json` file in the project root directory to include your specific configuration values. You can use the provided `config.sample.json` as a template:

- **vault_directory**: This is the path to the directory containing your Markdown files.

- **base_url**: This is the URL for the image hosting service used in markdown links. Replace `https://example.com/` with your own image hosting URL.

- **upload_url**: This is the URL of the PicList/PicGo service that will handle the image uploads. Replace `http://127.0.0.1:36677/upload` with the actual URL of your upload service.

- **cleanup**: Determines whether local images should be deleted after they are uploaded. Set it to `true` if you want to clean up local images, or `false` to keep them.

- **test_vault_dir**: This is the path to a directory used for testing purposes, intended for unit tests only.

- **test_upload_url**: This is the URL used for testing the upload functionality, intended for unit tests only.

Ensure that all paths and URLs are correctly set according to your environment and requirements. This configuration file is crucial for the script to function correctly, as it dictates where to find the Markdown files, where to upload the images, and how to handle the images post-upload.

#### Running Tests

To run the unit tests, use the following command:

```bash
poetry run pytest
```
