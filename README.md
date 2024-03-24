Dont go into any directory
just run the below commands in the main directory:

### Might not work

## Command to create images 
```
docker build -t user-management-service:v1 ./user_management_service && \
docker build -t product-management-service:v1 ./product_management_service && \
docker build -t order-management-service:v1 ./order_management_service

```

## Command to deploy all microservices 
```
kubectl apply -f user-management-service/user-management-deployment.yaml \
              -f product-management-service/product-management-deployment.yaml \
              -f order-management-service/order-management-deployment.yaml
```

