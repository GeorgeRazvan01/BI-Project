from flask import Flask, jsonify
from db import get_sales_by_decoration_type

app = Flask(__name__)

# Define API endpoint
@app.route('/api/sales/decoration_type', methods=['GET'])
def sales_by_decoration_type():
    sales = get_sales_by_decoration_type()
    return jsonify(sales)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)

