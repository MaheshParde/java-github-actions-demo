FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY target/java-github-actions-demo-1.0-SNAPSHOT.jar java-github-actions-demo-1.0-SNAPSHOT.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "java-github-actions-demo-1.0-SNAPSHOT.jar"]

