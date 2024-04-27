from flask import Flask, request, jsonify, render_template

app = Flask(__name__)   

# Example dataset
dataset = [
    {"title": "The Coal Mines Act, 1952", "description": "An act to regulate the working conditions in coal mines and improve safety measures for workers."},
    {"title": "Indian Explosives Act, 1884", "description": "Legislation governing the manufacture, possession, use, sale, transport, import, and export of explosives in India."},
    {"title": "Colliery Control Order, 2000", "description": "A regulatory order outlining safety and operational procedures for collieries."},
    {"title": "Colliery Control Rules, 2004", "description": "Rules specifying the procedures and standards for the management and operation of collieries."},
    {"title": "The Coal Mines Regulations, 2017", "description": "Regulations covering various aspects of coal mining operations, including safety, health, and environmental protection."},
    {"title": "The Payment of Wages (Mines) Rules, 1956", "description": "Rules governing the payment of wages to workers employed in mines."},
    {"title": "Land Acquisition Act (CBA)", "description": "Legislation governing the acquisition of land for mining purposes, including compensation and rehabilitation provisions."},
    {"title": "Land Acquisition (LA)", "description": "Regulations outlining procedures for the acquisition of land for various purposes, including mining."},
    {"title": "Resettlement and Rehabilitation (RandR)", "description": "Guidelines and regulations concerning the resettlement and rehabilitation of communities affected by mining activities."}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    query_text = data.get('query', '').lower()
    
    response = "Sorry, I couldn't find any relevant information for your query."
    
    # Search the dataset for matching titles or descriptions
    for item in dataset:
        if query_text in item['title'].lower() or query_text in item['description'].lower():
            response = f"Title: {item['title']}\nDescription: {item['description']}"
            break
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
