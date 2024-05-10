
# Vendor Management System with Performance Metrics



Vendor Management System with Performance Metrics
Objective:
Develop a Vendor Management System using Django and Django REST Framework. This system will handle vendor 
With JWT token Authentication
## Installation

If downloaded zip file

look for the virtual environment name

activate the venv 

    dev-env/Scripts/activate

    cd project name

    python manage.py makemigrations

    python manage.py migrate

# To Run the project on local host

    python manage.py runserver

# Create a Superuser 
    python manage.py createsuperuser



```
 
# API Reference

API Endpoints:

ALL Endpoints required jwt token

Generate jwt token 

To Create jwt token Endpoint
    POST /api/token/

#after generating token while hitting the rest of the urls 
#Go to autenciation section select type bearer token and put token there


Create a new vendor.

    POST /api/vendors/

 List all vendors

    GET /api/vendors/
  
Retrieve a specific vendor's details.

    GET /api/vendors/{vendor_id}/

 Update a vendor's details.

    PUT /api/vendors/{vendor_id}/

 Delete a vendor
    DELETE /api/vendors/{vendor_id}/
-------------------------------------------------------
              purchase order      Endpoints
-------------------------------------------------------
 Create a purchase order.
    POST /api/purchase_orders/

 List all purchase orders with an option to filter by
vendor.
    GET /api/purchase_orders/

 Retrieve details of a specific purchase order.
    GET /api/purchase_orders/{po_id}/

 Update a purchase order.
    PUT /api/purchase_orders/{po_id}/

 Delete a purchase order.
    DELETE /api/purchase_orders/{po_id}/

-------------------------------------------------------
Retrieve a vendor's performance
metrics.

    GET /api/vendors/{vendor_id}/performance

vendors to acknowledge POs

    POST /api/purchase_orders/{po_id}/acknowledge


