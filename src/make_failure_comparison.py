"""Tạo ảnh so sánh baseline và yaw drift 3° cho frame KITTI 000011."""
from pathlib import Path

import cv2


ROOT = Path("results/figures")
BASELINE = ROOT / "overlay_000011_r0.0_p0.0_y0.0_t0.0_0.0_0.0.png"
DRIFT = ROOT / "overlay_000011_r0.0_p0.0_y3.0_t0.0_0.0_0.0.png"
OUTPUT = ROOT / "fail_02_yaw_3deg_000011.png"


def main() -> None:
    images = [cv2.imread(str(path)) for path in (BASELINE, DRIFT)]
    if any(image is None for image in images):
        raise FileNotFoundError("Hãy tạo hai ảnh overlay baseline và yaw 3° trước")
    if images[0].shape != images[1].shape:
        raise ValueError("Hai ảnh overlay phải có cùng kích thước")

    panels = []
    for image, title in zip(images, ("Baseline: yaw 0 deg", "Perturbed calibration: yaw +3 deg")):
        panel = image.copy()
        cv2.rectangle(panel, (0, 0), (panel.shape[1], 46), (20, 20, 20), -1)
        cv2.putText(panel, title, (14, 32), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (255, 255, 255), 2, cv2.LINE_AA)
        panels.append(cv2.copyMakeBorder(panel, 0, 0, 0, 4, cv2.BORDER_CONSTANT,
                                         value=(255, 255, 255)))
    if not cv2.imwrite(str(OUTPUT), cv2.hconcat(panels)):
        raise OSError(f"Không ghi được ảnh {OUTPUT}")
    print(f"-> {OUTPUT}")


if __name__ == "__main__":
    main()
