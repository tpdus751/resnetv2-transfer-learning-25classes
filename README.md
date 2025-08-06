# ResNetV2 기반 25개 클래스 이미지 분류기

InceptionResNetV2와 전이학습을 활용하여, 총 25개의 일상 사물 및 자동차 이미지를 분류하는 이미지 분류 모델입니다.  
직접 수집한 데이터를 기반으로 학습하였으며, 검증 정확도 97% 이상을 달성했습니다.

---

## 프로젝트 구조
```
resized_dataset/
├── train_split/
├── validation_split/
└── test/
ResNetV2_25_Classification_seyeon.ipynb
```

---

##  클래스 목록 (총 25개)

```
식물 : corn, egg, hot, potato, tomato
생활 용품 : 노트, 노트북 , 마우스, 보조배터리, 애플워치, 에어팟, 우산, 잔스포츠 백팩, 필통(필기구), 지갑,
과자 : 마가렛트, 사탕, 빈츠, 몽쉘, 초코하임
자동차 : 밴, 대형suv, 소형,  중소형suv, 중형세단  
```

---

## 데이터셋 구성

- 총 5명이 각자 5개 클래스씩 이미지 직접 수집
- 클래스당 이미지 수:
  - 학습(train): 80장
  - 검증(validation): 20장
  - 테스트(test): 10장
- 다양한 사물 및 차량 포함

---

## 모델 구조 및 설정

- Base 모델: `InceptionResNetV2` (ImageNet 사전학습, include_top=False)
- 출력층 구성:
  - `GlobalAveragePooling2D → Dropout(0.5) → Dense(1024, relu) → Dropout(0.5) → Dense(25, softmax)`
- Optimizer: Adam (`learning_rate=0.0001`)
- 손실 함수: categorical_crossentropy
- 입력 이미지 크기: 224 x 224
- Epoch: 최대 500 (EarlyStopping 적용)

---

## 포함된 파일 설명

| 파일명 | 설명 |
|--------|------|
| `ResNetV2_25_Classification_seyeon.ipynb` | 전체 모델 학습, 평가, 시각화가 포함된 Jupyter Notebook |
| `resized_dataset/` | 전처리된 이미지 데이터셋 (224x224 리사이즈), `train_split`, `validation_split`, `test` 폴더 포함 |

---

## 성능 요약

<img width="1136" height="215" alt="image" src="https://github.com/user-attachments/assets/47b3de5b-c3d7-43e0-918d-4ccbebad990f" />


| 항목 | 값 |
|------|----|
| 최종 Epoch | 71 |
| 학습 정확도 | 96.9% |
| 검증 정확도 | **97.8%** |
| 검증 손실 | 0.0562 |
| 테스트 정확도 | 약 90% |
| Macro F1 Score (테스트) | 약 0.77 |

---

## 결과 시각화

### 정확도 및 손실 변화
<Figure size 1200x500 with 2 Axes><img width="800" height="490" alt="image" src="https://github.com/user-attachments/assets/f5f4d611-4db4-4dfe-ac3c-e8ca039905a3" />

### Validation 데이터 혼동 행렬
<Figure size 1200x1000 with 2 Axes><img width="800" height="989" alt="image" src="https://github.com/user-attachments/assets/a8cf366c-5c40-4373-a93f-2c59476f894b" />

### Test 데이터 혼동 행렬
<Figure size 1400x1200 with 2 Axes><img width="800" height="1190" alt="image" src="https://github.com/user-attachments/assets/4ff990f7-7295-43ad-8df3-159966081458" />

### Test 예측 확인 예시
<img width="800" height="962" alt="image" src="https://github.com/user-attachments/assets/63ff0300-29cf-4075-b715-09877f9774c3" />
<img width="800" height="749" alt="image" src="https://github.com/user-attachments/assets/3cb6948c-76fb-4da2-8354-e45dbac6b391" />
<img width="800" height="748" alt="image" src="https://github.com/user-attachments/assets/6c0f1da9-901f-447c-9770-d9a6000f4df8" />

### Classification Report
<img width="800" height="681" alt="image" src="https://github.com/user-attachments/assets/92366f34-7bd3-4ca0-b63b-4f5e64dbc548" />


> 💡 이미지 캡처는 VSCode 환경에서 수행하였습니다.

---

## 실행 방법

1. Jupyter Notebook 환경에서 실행
2. `ResNetV2_25_Classification_seyeon.ipynb` 열기
3. 필요한 라이브러리 설치:
   ```bash
   pip install tensorflow numpy pandas scikit-learn seaborn matplotlib
   ```
셀을 순서대로 실행하여 학습 또는 추론 진행

⚠️ 한계점 및 개선 방향

<img width="1406" height="800" alt="image" src="https://github.com/user-attachments/assets/1286e9a6-aba7-4563-8368-7fb2d20b7bbc" />

일부 클래스(애플위치, 에어팟 등)는 샘플 수가 적어 테스트 성능이 낮게 나타남

<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/31fc202f-3876-4531-8b4c-ec4dcc2bc890" />

특정 구도에서만 찍힌 데이터로 인해 과적합 가능성 존재

더 다양한 각도, 배경, 환경에서의 이미지 수집 시 일반화 성능 향상 가능

활용 목적
- 인공지능 실습 과제 및 시험 제출용 프로젝트
- 전이학습 및 멀티클래스 분류 모델 구축 경험 목적

🙋‍♀️ 기여자(이미지 수집)
이미지 수집 및 모델 개발: 총 5명
- 박세연, 김범준, 이예은, 전가람, 김시원

