from flask import Flask, request, jsonify , render_template
from flask_cors import CORS
from sql_connection import get_sql_connection
import json
import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)
CORS(app)

connection = get_sql_connection()

@app.route('/getUOM', methods=['GET'])
def get_uom():
    try:
        response = uom_dao.get_uoms(connection)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/getProducts', methods=['GET'])
def get_products():
    try:
        response = products_dao.get_all_products(connection)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    try:
        request_payload = json.loads(request.form['data'])
        product_id = products_dao.insert_new_product(connection, request_payload)
        return jsonify({'product_id': product_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# @app.route('/getAllOrders', methods=['GET'])
# def get_all_orders():
#     try:
#         response = orders_dao.get_all_orders(connection)
#         return jsonify(response)
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM orders")  # Example query
        orders = cursor.fetchall()
        return jsonify(orders)
    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    try:
        request_payload = json.loads(request.form['data'])
        order_id = orders_dao.insert_order(connection, request_payload)
        return jsonify({'order_id': order_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    try:
        return_id = products_dao.delete_product(connection, request.form['product_id'])
        return jsonify({'product_id': return_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ui/manage-product')
def manage_product():
    return render_template('manage-product.html')

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)