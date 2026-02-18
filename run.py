from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from backend.lexer import lexical_analyze
from backend.syntax import syntax_analyze

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('lexical_analysis')
def handle_analyze_code(data):
    code = data.get('code', '')
    if not code.strip():
        emit('lexical_result', {'tokens': [], 'errors': ['No input detected.']})
        return
    
    # Call lexer function
    tokens, errors = lexical_analyze(code)
    
    # Convert tokens to dicts for JSON serialization 
    token_dicts = [{'type': token.type, 'value': token.value} for token in tokens]

    err_dicts = [str(error) for error in errors]

    # Emit result back to the frontend
    emit('lexical_result', {'tokens': token_dicts, 'errors': err_dicts})

@socketio.on('syntax_analysis')
def handle_syntax_analysis(data):
    code = data.get('code', '')
    tokens, lexical_err = lexical_analyze(code)

    if lexical_err:
        emit('syntax_result', {'sucess': False, 'error': 'Syntax Error due to Lexical Errors'})
        return

    msg, syntax_err = syntax_analyze(tokens)
    if syntax_err:
        emit('syntax_result', {'success': False, 'error': str(syntax_err)})
    else:
        emit('syntax_result', {'success': True, 'msg': msg})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)