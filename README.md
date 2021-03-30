# Tensorflow Model Deployment With Docker 

The command to run the docker container is

```docker run -p 8501:8501 --name tfserving_nlp --mount type=bind,source=/where/the/model_is_saved,target=/models/nlp_model -e MODEL_NAME=nlp_model -t tensorflow/serving &
```

When you run requests_tf.py, you should get a dict as a result