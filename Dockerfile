FROM tensorflow/serving:latest
COPY ./src/models/saved_model /tfserving
# Expose ports
# gRPC
EXPOSE 8500
# REST
EXPOSE 8501
ENTRYPOINT ["/usr/bin/tf_serving_entrypoint.sh"]
CMD ["--model_name=iana", "--model_base_path=/tfserving/iana"]