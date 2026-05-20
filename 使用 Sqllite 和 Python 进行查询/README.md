# Python + SQLite 数据库查询与分析

这是一个基于 Python 的 SQLite 数据库分析练习项目。它使用 `sqlite3` 连接 Chinook 示例数据库，通过 SQL 查询和 `pandas` 进行数据分析，并使用 `matplotlib` 将结果可视化。

## 项目目标
- 练习使用 `sqlite3` 连接和操作 SQLite 数据库。
- 练习使用 `pandas` 执行 SQL 查询并处理结果集。
- 学习探索数据库模式（Schema）的方法（查看表结构、字段类型、主外键关系）。
- 学习通过 SQL 多表关联查询回答业务问题。
- 学习使用 `matplotlib` 将分析结果以柱状图等形式直观展示。

## 功能特性
- 自动读取 Chinook 数据库全部表名及结构。
- 探索核心表的前几行数据，快速理解数据内容。
- **分析 1：销量排名前十的歌曲** — 通过 `Track` 与 `InvoiceLine` 表关联，统计每首歌的购买次数并排序。
- **分析 2：各国销售收入排名** — 按国家分组汇总 `Invoice` 总收入，找出收入最高的市场。
- **分析 3：销售员工业绩排名** — 通过 `Employee`、`Customer`、`Invoice` 三表关联，计算每位销售代理的总销售额。
- 每个分析结果都配有柱状图可视化。
- 结果直接展示在 Jupyter Notebook 中，无需额外导出。

## 技术栈
- **Python 3.x**
- **sqlite3**: 连接和查询 SQLite 数据库。
- **pandas**: 执行 SQL 查询、处理和分析数据。
- **matplotlib**: 将分析结果绘制为统计图表。

## 数据库说明
本项目使用 Chinook 示例数据库（`chinook.db`），该数据库模拟了一个数字音乐商店的业务场景，包含以下核心表：

| 表名 | 说明 |
|------|------|
| Artist | 艺术家信息 |
| Album | 专辑信息 |
| Track | 曲目信息（含时长、价格等） |
| Genre | 音乐流派 |
| MediaType | 媒体格式类型 |
| Employee | 员工信息 |
| Customer | 客户信息 |
| Invoice | 发票/订单 |
| InvoiceLine | 发票明细（订单中的每首曲目） |
| Playlist | 播放列表 |
| PlaylistTrack | 播放列表与曲目的关联 |

