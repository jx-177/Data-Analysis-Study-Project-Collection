#  Python 职位列表抓取器

这是一个基于 Python 的网页爬虫练习项目。它从 [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) 网站抓取招聘信息，并将结果保存为 CSV 文件。

## 项目目标
- 练习使用 `requests` 获取网页内容。
- 练习使用 `BeautifulSoup` 解析 HTML 结构。
- 学习如何提取特定字段（标题、公司、地点、链接）。
- 学习如何将结构化数据存储到 CSV 文件中。

## 功能特性
- 自动抓取页面上所有的职位列表。
- 提取字段：**职位名称 (Job Title)**、**公司名称 (Company)**、**工作地点 (Location)**、**详情链接 (URL)**。
- 结果持久化存储为 `jobs.csv`。
- 包含简单的错误处理逻辑。

## 技术栈
- **Python 3.x**
- **Requests**: 发送 HTTP 请求。
- **Beautiful Soup 4**: 解析 HTML 文档。
- **CSV 模块**: 处理数据导出。