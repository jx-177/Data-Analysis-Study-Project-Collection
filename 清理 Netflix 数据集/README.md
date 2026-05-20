# Netflix 数据集清洗 — 数据预处理与标准化

这是一个基于 Python 的 Netflix 影视数据集清洗项目。它使用 `pandas` 对 Netflix 电影和电视节目数据进行全面的数据质量审查和预处理，包括缺失值识别与填充、混合类型列拆分、日期格式标准化等，最终输出一份可直接用于后续分析建模的干净数据集。

## 项目目标
- 练习使用 `pandas` 加载 CSV 数据并进行初步的数据探索（形状、类型、缺失值）。
- 学习数据清洗的基本方法：缺失值识别、缺失率计算及多种填充策略（常量填充、前向填充、众数填充、删除）。
- 掌握混合类型列的拆分与规范化处理（如将 `"90 min"` 拆分为数值 `90` 和单位 `Minutes`）。
- 练习将字符串日期列解析为 `datetime` 类型，便于时间序列分析。
- 输出清洗后的数据集，为后续分析和建模做好准备。

## 功能特性
- 自动读取 Netflix 数据集（`netflix_titles.csv`），展示列名与数据结构。
- 输出数据统计描述（`describe`、`info`）及前 5 行预览。
- 对缺失值进行针对性处理：
  - **Director（导演）**：缺失率 29.9%，填充为 `"Unknown"`。
  - **Cast（演员）**：缺失率 9.4%，填充为 `"Not Available"`。
  - **Country（国家）**：缺失率 9.4%，填充为 `"Unknown"`。
  - **Date_added（添加日期）**：缺失 10 个值，使用前向填充（`ffill`）。
  - **Rating（评级）**：缺失 4 个值，使用众数填充。
  - **Duration（时长）**：缺失 3 个值，直接删除对应行。
- 拆分混合类型列 `duration`：
  - `duration_value`：提取数值部分（如 90）并转换为数值类型。
  - `duration_type`：提取单位部分并统一格式（`min` → `Minutes`，`Season`/`Seasons` → `Seasons`）。
- 将 `date_added` 列解析为 `datetime` 类型，无法解析的设为 `NaT`。
- 将清洗后的数据保存为 `cleaned-data.csv`。

## 技术栈
- **Python 3.x**
- **pandas**：数据读取、清洗、缺失值处理与类型转换。

## 数据集说明
本项目使用从 Kaggle 获取的 Netflix 影视数据集（`archive/netflix_titles.csv`），记录了 8807 条 Netflix 电影和电视节目的元数据信息，包含以下字段：

| 列名 | 说明 |
|------|------|
| show_id | 节目 ID |
| type | 类型（Movie = 电影，TV Show = 电视节目） |
| title | 标题 |
| director | 导演 |
| cast | 演员阵容 |
| country | 制作国家 |
| date_added | 添加至 Netflix 的日期 |
| release_year | 发行年份 |
| rating | 内容评级（如 PG-13、TV-MA 等） |
| duration | 时长（电影以分钟计，电视节目以季数计） |
| listed_in | 内容分类/类型标签 |
| description | 内容简介 |

## 清洗结果
- 原始数据：8807 行 × 12 列，清洗后：8804 行 × 14 列（新增 `duration_value` 和 `duration_type` 两列）。
- 所有缺失值已处理完毕，`date_added` 列已转为标准日期格式，`duration` 列已完成拆分与规范化。
- 清洗后的数据保存为 `cleaned-data.csv`，可直接用于后续的数据分析和可视化任务。
