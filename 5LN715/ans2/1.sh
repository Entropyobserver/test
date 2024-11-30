> merged.txt  # 清空目标文件，防止内容累加
for i in {1..20}; do
    cat sentence$i.txt >> merged.txt
done