import requests
from bs4 import BeautifulSoup
import csv
import os


def scrape_jobs():
    URL = "https://realpython.github.io/fake-jobs/"

    print(f"正在请求页面: {URL}...")

    try:
        # 1. 发送网络请求
        response = requests.get(URL)
        response.raise_for_status()  # 检查请求是否成功

        # 2. 解析 HTML
        soup = BeautifulSoup(response.content, "html.parser")


        # 3. 定位职位容器
        # 观察网页结构可知，每个职位都包裹在 class 为 "card-content" 的 div 中
        job_elements = soup.find_all("div", class_="card-content")

        jobs_data = []

        print(f"解析成功，发现 {len(job_elements)} 条职位信息。")

        # 4. 遍历提取数据
        for job_element in job_elements:
            title_element = job_element.find("h2", class_="title")
            company_element = job_element.find("h3", class_="company")
            location_element = job_element.find("p", class_="location")

            # 提取链接：链接通常在底部的 'footer' 部分，查找带有 'Apply' 字样的 <a> 标签
            link_element = job_element.find_all("a")[1]  # 第二个链接通常是详情页链接

            # 清洗数据（处理缺失值和空格）
            title = title_element.text.strip() if title_element else "N/A"
            company = company_element.text.strip() if company_element else "N/A"
            location = location_element.text.strip() if location_element else "N/A"
            link = link_element["href"] if link_element else "N/A"

            jobs_data.append({
                "Job Title": title,
                "Company": company,
                "Location": location,
                "URL": link
            })

        # 5. 保存到 CSV
        save_to_csv(jobs_data)

    except Exception as e:
        print(f"发生错误: {e}")


def save_to_csv(data):
    filename = "jobs.csv"
    keys = data[0].keys() if data else []

    if not keys:
        print("没有抓取到数据，停止保存。")
        return

    try:
        with open(filename, "w", newline="", encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

        print(f"数据已成功保存至: {os.path.abspath(filename)}")
    except IOError as e:
        print(f"文件写入失败: {e}")


if __name__ == "__main__":
    scrape_jobs()