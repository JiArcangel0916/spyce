import { useEffect, useState } from "react";
import { io, Socket } from 'socket.io-client';
import { Token } from './utils/tokenInterface';
import { Header } from './components/Header';
import { CodeEditor } from './components/CodeEditor';
import { Terminal } from './components/Terminal';
import { LexicalTable } from "./components/LexicalTable";
import './styles/Main.css';

export default function App() {
  const [code, setCode] = useState("spyce() -> void {\n\tsay('Hello, World!');\n\tgiveback void;\n}");
  const [tokens, setTokens] = useState<Token[]>([]);
  const [terminalMsg, setTerminalMsg] = useState("");
  const [showLexical, setShowLexical] = useState(false);
  const [socket, setSocket] = useState<Socket | null>(null);

  useEffect(() => {
    const newSocket = io('http://localhost:5000');
    setSocket(newSocket);

    // LEXICAL SOCKET
    newSocket.on('lexical_result', (data: {
      tokens: { type: string, value: string }[];
      errors: string[];
    }) => {
      setTimeout(() => {
        const formattedTokens: Token[] = data.tokens.map(t => ({
          lexeme: t.value,
          token: t.type
        }));

        setTokens(formattedTokens);

        if (data.errors.length > 0) {
          const formattedErrors = data.errors.join('\n');
          setTerminalMsg(`❌ Errors:\n${formattedErrors}`);
        } else {
          setTerminalMsg(`✅ Lexical Analysis Successful`);
        }
      }, 600);
    });

    // SYNTAX SOCKET
    newSocket.on('syntax_result', (data: {
      success: boolean,
      error?: string;
      msg?: string
    }) => {
      setTimeout(() => {
        if (data.success) {
          setTerminalMsg(data.msg || `✅ Syntax Analysis Successful`);
        } else {
          setTerminalMsg(`❌ ${data.error}`);
        }
      }, 600);
    });

    return () => {
      newSocket.disconnect();
    }
  }, []);

  const analyzeLexer = () => {
    if (!socket || !socket.connected) {
      setTerminalMsg('❌ Socket not connected');
      return;
    }

    if (code.trim() === "") {
      setTerminalMsg("⚠️ No input detected.")
      setTokens([]);
      return
    }
    setTerminalMsg("⏳ Running Lexical Analysis...");
    setShowLexical(!showLexical);

    socket.emit('lexical_analysis', { code });
  };

  const analyzeSyntax = () => {
    if (!socket || !socket.connected) {
      setTerminalMsg('❌ Socket not connected');
      return;
    }
    if (code.trim() === "") {
      setTerminalMsg("⚠️ No input detected.")
      setTokens([]);
      return
    }
    setTerminalMsg("⏳ Running Syntax Analysis...");

    socket.emit('syntax_analysis', { code })
  };

  return (
    <main>
      <div className="HeaderWrapper">
        <Header
          onRun={() => { analyzeLexer(); analyzeSyntax(); }}
          onLexical={analyzeLexer}
          onSyntax={analyzeSyntax}
        />
      </div>

      <div className="CodeEditorWrapper">
        <CodeEditor
          code={code}
          setCode={setCode}
          showLexical={showLexical}
        />
      </div>

      <LexicalTable
        tokens={tokens}
        showLexical={showLexical}
      />

      <div className="TerminalWrapper">
        <Terminal message={terminalMsg} showLexical={showLexical} />
      </div>
    </main>
  );
}