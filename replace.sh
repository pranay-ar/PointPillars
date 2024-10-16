find pointpillars/ -type f -name "*.py" -exec sed -i 's/^from ops/from pointpillars.ops/g' {} +
find pointpillars/ -type f -name "*.py" -exec sed -i 's/^from utils/from pointpillars.utils/g' {} +
find pointpillars/ -type f -name "*.py" -exec sed -i 's/^from model/from pointpillars.model/g' {} +
find pointpillars/ -type f -name "*.py" -exec sed -i 's/^from loss/from pointpillars.loss/g' {} +
find pointpillars/ -type f -name "*.py" -exec sed -i 's/^from dataset/from pointpillars.dataset/g' {} +
