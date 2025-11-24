from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from backend.lexer import lexical_analyze

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('analyze_code')
def handle_analyze_code(data):
    code = data.get('code', '')
    if not code.strip():
        emit('analysis_result', {'tokens': [], 'errors': ['No input detected.']})
        return
    
    # Call your lexer function
    tokens, errors = lexical_analyze(code)
    
    # Convert tokens to dicts for JSON serialization (since Token objects aren't serializable)
    token_dicts = [{'type': token.type, 'value': token.value} for token in tokens]

    err_dicts = [str(error) for error in errors]
    error_dicts = [{
        'pos_start': {
            'idx': error.pos_start.idx,
            'ln': error.pos_start.ln,
            'col': error.pos_end.col,
        },
        'pos_end': {
            'idx': error.pos_end.idx,
            'ln': error.pos_end.ln,
            'col': error.pos_end.col,
            'fullText': error.pos_end.fullText
        },
        'error': error.error_name,
        'info': error.info
    } for error in errors]

    # Emit result back to the frontend
    emit('analysis_result', {'tokens': token_dicts, 'errors': err_dicts})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)