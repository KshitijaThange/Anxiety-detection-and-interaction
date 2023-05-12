from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

train_data_gen = ImageDataGenerator(rescale=1./255)
validation_data_gen = ImageDataGenerator(rescale=1./255)


train_generator = train_data_gen.flow_from_directory('data/train', target_size=(48, 48), batch_size=64, color_mode='grayscale', class_mode='categorical')

validation_generator = validation_data_gen.flow_from_directory('data/test', target_size=(48, 48), batch_size=64, color_mode='grayscale', class_mode='categorical')

# CNN Model
anxiety_model = Sequential()

anxiety_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
anxiety_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
anxiety_model.add(MaxPooling2D(pool_size=(2, 2)))
anxiety_model.add(Dropout(0.25))

anxiety_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
anxiety_model.add(MaxPooling2D(pool_size=(2, 2)))
anxiety_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
anxiety_model.add(MaxPooling2D(pool_size=(2, 2)))
anxiety_model.add(Dropout(0.25))

anxiety_model.add(Flatten())
anxiety_model.add(Dense(1024, activation='relu'))
anxiety_model.add(Dropout(0.5))
anxiety_model.add(Dense(3, activation='softmax'))

anxiety_model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.0001, decay=1e-6), metrics=['accuracy'])


# train CNN model

anxiety_model_info = anxiety_model.fit_generator(train_generator, steps_per_epoch=1200 // 64, epochs=100, validation_data=validation_generator, validation_steps=200 // 64)

#save model in json file
model_json = anxiety_model.to_json()
with open("anxiety_model.json", "w") as json_file:
    json_file.write(model_json)

# save trained model in .h5 file
anxiety_model.save_weights('anxiety_model.h5')



