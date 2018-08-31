import turicreate as tc
data = tc.image_analysis.load_images('image', with_path= True)
data['label'] = data['path'].apply(lambda path:'dog' if 'dog' in path else 'cat')

print(data.groupby('label', [tc.aggregate.COUNT]))

data.save('cats-dogs.sframe')

data.explore()

data = tc.SFrame('cats-dogs.sframe')
train_data, test_data = data.random_split(0.8)
model = tc.image_classifier.create(train_data, target='label', max_iterations=50)

predictions = model.predict(test_data)
metrics = model.evaluate(test_data)
print(metrics['accuracy'])

model.save('mymodel.model')
model.export_coreml('CatsAndDogs.mlmodel')