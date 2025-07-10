import json
import os

output_file = '/app/output/scores.json'
output_file = './scores.json'
if __name__ == '__main__':
    result = dict(score=0.0)
    json.dump(result, f, indent=4)
    print(f'Write result to {output_file}')
        
