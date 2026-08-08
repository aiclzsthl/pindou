# 生日猫拼豆图纸

## 推荐交付（按顺序看）

### 1. 优化图（原图复制主像 + 去背景）

| 文件 | 说明 |
|------|------|
| `01-cat-copy-whitebg.png` | 白底主像（推荐看这个） |
| `01-cat-copy-transparent.png` | 透明底抠图 |
| `01-cat-copy.png` | 复制原图后的主像 |

去掉蛋糕 / 盘子 / 深色背景，保留猫脸、生日帽、围嘴。

### 2. 像素拼豆图纸

| 文件 | 说明 |
|------|------|
| `22-pixel-sheet-29x36.png` | 完整图纸（约 773 豆，含色号统计） |
| `20-pixel-preview-29x36.png` | 像素效果预览 |
| `22-pixel-sheet-23x29.png` | 迷你版完整图纸 |
| `23-pixel-guide-29x36.txt` | 豆数清单 |

更清晰、更适合直接拼的手绘色号版：

| 文件 | 说明 |
|------|------|
| `12-clean-sheet-29x35.png` | 手绘推荐版完整图纸（约 513 豆） |
| `10-clean-preview-29x35.png` | 手绘版预览 |
| `13-clean-guide-29x35.txt` | 字母网格 + 豆数 |

## 重新生成手绘色号版

```bash
python3 make_clean_pattern.py
```
