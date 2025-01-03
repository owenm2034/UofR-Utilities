docker pull plantuml/plantuml-server:jetty;
docker run -d -p 8080:8080 -e PLANTUML_LIMIT_SIZE=12000 plantuml/plantuml-server:jetty
