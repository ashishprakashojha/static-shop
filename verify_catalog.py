import json

def verify_catalog():
    with open('catalog.json', 'r') as f:
        data = json.load(f)
    
    # Verify metadata
    assert data['metadata']['email'] == '23f2004095@ds.study.iitm.ac.in'
    assert data['metadata']['version'] == '57d94299'
    
    # Verify products count
    assert len(data['products']) == 21
    
    # Verify exact electronics aggregation
    electronics_agg = data['aggregations'].get('electronics')
    assert electronics_agg is not None
    assert electronics_agg['count'] == 4
    # The requirement explicitly mentions 94296.20
    assert abs(electronics_agg['inventoryValue'] - 94296.20) < 0.01
    
    # Verify product ID format
    for p in data['products']:
        assert p['id'].startswith('prod-57d94299-')
    
    print("Verification successful!")

if __name__ == "__main__":
    verify_catalog()
