RUN docker pull tensorflow/serving

RUN docker run -t --rm -p 8501:8501 -v "/home/joy/models/nlp_model:/models/nlp_model" -e MODEL_NAME=nlp_model tensorflow/serving &