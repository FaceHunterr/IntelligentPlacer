# IntelligentPlacer

## Общее описание
На вход алгоритма поступает изображение горизонтальной ровной светлой поверхности, на которой расположены несколько небольших предметов и рядом белый бумажный лист с нарисованным на нём чёрным маркером выпуклым многоугольником. На выходе даётся ответ на вопрос: можно ли разместить указанные предметы на плоскости так, чтобы они все поместились внутри многоугольника.

## Требования ко входным данным
### Поверхность
- должна быть ровной, светлой и без рисунков
### Предметы
- расположены в нижней половине изображения и полностью влезают в кадр
- не перекрывают друг друга и белый лист, на котором нарисован многоугольник
- контраст предметов различения с фоном должен превышать 0.3
- предмет может находится на разных фотографиях
- на одном рисунке не может лежать 2 одинаковых предмета
- предмет должен иметь постоянную форму
### Многоугольник
- должен быть нарисован на белом бумажном листе А4
- нарисован чёрным маркером, его границы должны быть отчётливо видны (то есть в них не должно быть пробелов)
- должен быть выпуклым
- количество вершин от 3 до 8
### Камера
- должна располагаться на расстоянии 35-40 см от поверхности и под прямым углом к ней
### Источник света
- должен быть искусственным (например, лампа)
- должен располагаться так, чтобы предметы не отбрасывали тень на поверхность и чтобы не было теней от посторонних вещей (например, камеры)
- цвет света должен быть белым/жёлтым/оранжевым
### Изображение
- Разрешение должно быть 3000 на 4000
- Изображен не должно быть размыто (Максимальный тангенс угла наклона профиля яркости изображения на границе перепада не превышает 30)
## Требования к выходным данным
Ответ "Да" (True), если все предметы на изображении одновременно помещаются в многоугольник, не перекрывая друг друга. Иначе возвращается "Нет" (False).
## Фотографии предметов и поверхности
![image](https://user-images.githubusercontent.com/60978690/153725793-db8c9ead-e043-4ce1-95e1-9dfb3e09ef04.jpg)
![image](https://user-images.githubusercontent.com/60978690/153725695-08abf3df-f920-440a-93fe-e4a54f3d7a55.png)
![image](https://user-images.githubusercontent.com/60978690/153726137-972920c1-2993-40a5-88ae-0854130a0ecd.png)
![image](https://user-images.githubusercontent.com/60978690/153726143-d982c650-ff23-4f8d-ad23-1b051eb638eb.png)
![image](https://user-images.githubusercontent.com/60978690/153726155-2c571cd9-ce4d-4d3a-8b05-6f52d55ddb5f.png)
![image](https://user-images.githubusercontent.com/60978690/153726167-57f0d601-b17f-449b-b199-88d3a0cee164.png)
![image](https://user-images.githubusercontent.com/60978690/153726173-95092b6a-caef-47e1-81b7-11d79b23fe31.png)
![image](https://user-images.githubusercontent.com/60978690/153726176-8d3aeb36-c5cc-4c42-b0a5-249e52dc8532.png)
![image](https://user-images.githubusercontent.com/60978690/153726187-10aac9e9-c411-4253-b0d4-ef9ba339172c.png)
![image](https://user-images.githubusercontent.com/60978690/153726193-6f57f9fc-8064-4f42-8ccf-5e6e9bb1096f.png)
![image](https://user-images.githubusercontent.com/60978690/153726200-6be4fa5a-9515-414f-ab79-6ea1e424bff3.png)

![3_1_0](https://user-images.githubusercontent.com/60978690/153761856-8a9e077c-c0f5-49fb-b0f0-1051d534159b.jpg)
![3_1_0_big](https://user-images.githubusercontent.com/60978690/153761860-e266946f-1401-462f-8d27-513f46b914d1.jpg)
![3_1_1](https://user-images.githubusercontent.com/60978690/153761864-95b4eb9a-d801-4f7e-afb7-67fd711ce57c.jpg)
![3_2_1](https://user-images.githubusercontent.com/60978690/153761866-4f7e3d64-c78a-4eea-9bb6-c80d715c6915.jpg)
![4_1_0](https://user-images.githubusercontent.com/60978690/153761868-6542d41c-0f30-4eb6-93e5-cceba57c0f87.jpg)
![4_3_1](https://user-images.githubusercontent.com/60978690/153762282-f2156549-0c95-4f29-bee2-76bc3b36aaae.jpg)
![4_4_0](https://user-im![8_1_0](https://user-images.githubusercontent.com/60978690/153762348-6beb4b39-ea43-4a44-b5de-4a3364a3418a.jpg)ages.githubusercontent.com/60978690/153762295-4562d950-9999-4694-9dbb-4d1a82d7fe6d.jpg)
![5_1_0](https://user-images.githubusercontent.com/60978690/153762304-c6be82af-4112-4194-95a3-30503529c335.jpg)
![5_1_1](https://user-images.githubusercontent.com/60978690/153762307-db76763c-2654-4348-8dff-a3ed49d85a40.jpg)
![6_1_0](https://user-images.githubusercontent.com/60978690/153762310-11e39466-1753-430c-9460-c4c97d331501.jpg)
![6_2_1](https://user-images.githubusercontent.com/60978690/153762312-c2113417-16d2-49cf-a8fd-5a0a9782e8d3.jpg)
![6_5_1](https://user-images.githubusercontent.com/60978690/153762317-19684353-8dc6-4a46-9f08-489c7ffc4227.jpg)
![6_6_0](https://user-images.githubusercontent.com/60978690/153762322-44050536-c4bb-4492-8f73-66e8978e4017.jpg)
![7_1_1](https://user-images.githubusercontent.com/60978690/153762327-441780e3-2c95-403c-9576-b82a8bfee222.jpg)
![7_2_0](https://user-images.githubusercontent.com/60978690/153762329-ae4f183a-5f7f-41c3-9548-0d1f10ee6988.jpg)
![7_3_1](https://user-images.githubusercontent.com/60978690/153762331-19f9d76c-ca07-46ad-a48f-af49148696a8.jpg)
![8_1_0](https://user-images.githubusercontent.com/60978690/153762414-c4f4ec24-ea9e-4cdc-afde-44bb91e64719.jpg)
![8_1_0_big](https://user-images.githubusercontent.com/60978690/153762419-19b5f714-3748-4c2d-946c-58bb32dfdac5.jpg)
![8_1_1](https://user-images.githubusercontent.com/60978690/153762423-aef68791-7933-4a9c-9eb4-f222398cde53.jpg)
![8_2_1](https://user-images.githubusercontent.com/60978690/153762431-42c36edc-0f07-4b4e-a0cc-45bf0c46896d.jpg)
![big_2_1](https://user-images.githubusercontent.com/60978690/153762499-59f7a6f9-1367-476b-af71-a38ee70f8225.jpg)
![big_2_1_small](https://user-images.githubusercontent.com/60978690/153762502-9a669aaf-2a99-4824-a9ea-e6668a9b5bfe.jpg)
![big_6_1](https://user-images.githubusercontent.com/60978690/153762509-74a4f204-ba0b-43db-a488-5dc7ec0e1f87.jpg)
![big_7_0](https://user-images.githubusercontent.com/60978690/153762514-ffdae612-f280-4c9f-ad9f-6f230cce12c8.jpg)
![bad_1](https://user-images.githubusercontent.com/60978690/153762541-57dec34b-8b62-48b6-8392-ee5f1892f5f7.jpg)
![bad_2](https://user-images.githubusercontent.com/60978690/153762544-e601c9a4-76f9-477f-a8d4-ed1a973e0359.jpg)
![bad_3](https://user-images.githubusercontent.com/60978690/153762548-bc07a5e6-c424-468e-867f-0c90aec7150d.jpg)
![bad_4](https://user-images.githubusercontent.com/60978690/153762551-ef107182-65a7-4edb-bbab-3088d25c710b.jpg)
![bad_5](https://user-images.githubusercontent.com/60978690/153762556-1c65ac84-2b46-448d-bcbb-61cfbd4dd6e2.jpg)
![bad_6](https://user-images.githubusercontent.com/60978690/153762557-e6e047e8-8e1d-45d6-a9d0-bd397275b69e.jpg)
![bad_7](https://user-images.githubusercontent.com/60978690/153762561-6e655939-bb6a-4017-8f16-346d20d8cbd1.jpg)
![bad_8](https://user-images.githubusercontent.com/60978690/153762564-946c6c88-9685-4123-9bd9-38d411cf04e9.jpg)
![bad_9](https://user-images.githubusercontent.com/60978690/153762569-45753787-556c-45f5-873a-0d03ca24fbad.jpg)
![bad_10](https://user-images.githubusercontent.com/60978690/153762573-761ad637-4d1b-48a8-b4c4-da30e52137cf.jpg)
![bad_11](https://user-images.githubusercontent.com/60978690/153762575-ca190b69-0784-4aa0-aa9b-17f9f69214fc.jpg)
![bad_12](https://user-images.githubusercontent.com/60978690/153762577-46c3b8f9-f37c-44bb-a9d0-d7e18aa51219.jpg)
![bad_13](https://user-images.githubusercontent.com/60978690/153762582-1b659a0a-a05e-4e44-89bf-4a936f1515f7.jpg)




