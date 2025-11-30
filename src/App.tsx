import { useEffect, useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlay } from "@fortawesome/free-solid-svg-icons";
import { io, Socket } from 'socket.io-client';
import "./App.css";

// Type definition for tokens
interface Token {
  lexeme: string;   // The actual text extracted from code
  token: string;    // Token type
}

function App() {
  // -------- State Variables ---------
  const [code, setCode] = useState("");                       // Stores user input code
  const [tokens, setTokens] = useState<Token[]>([]);          // Stores the list of tokens from lexical analysis
  const [terminalMsg, setTerminalMsg] = useState("");         // Displays messages (success, warnings) in terminal
  const [showLexical, setShowLexical] = useState(false);      // Controls visibility of the lexical table (toggle)
  const [socket, setSocket] = useState<Socket | null>(null);  // Socket state

  // Toggle function for showing/hiding lexical table
  const handleLexicalClick = () => setShowLexical(!showLexical);

  // Lock page scrolling while the code editor is active
  useEffect(() => {
    document.body.style.overflow = "hidden";
    
    const newSocket = io('http://localhost:5000');
    setSocket(newSocket);
    newSocket.on('analysis_result', (data: {
      tokens: { 
        type: string; 
        value: string; 
      }[];
        errors: string[];
    }) => {
        const formattedTokens: Token[] = data.tokens.map(t => ({
          lexeme: t.value,
          token: t.type
        }));
      
      setTokens(formattedTokens);

      if (data.errors.length > 0){
        const formattedErrors = data.errors.join('\n');
        setTerminalMsg(`❌ Errors:\n${formattedErrors}`)
      } else {
        setTerminalMsg(`✅ Lexical Analysis Successful`)
      }
    });

    return () => {
    document.body.style.overflow = "auto";    // Restore scroll on unmount
    newSocket.disconnect()
  };
}, []);


//----------------------------------------------
  // -------------------------
  // FUNCTION: Syntax Highlighting (COLOR CODING NUNG CODE)
  // Converts code text into HTML with color-coded spans for display
  // Highlights keywords, strings, numbers, operators, comments, and identifiers
  // -------------------------
  function highlightCode(input: string): string {
    if (!input) return "";

    const escapeHtml = (s: string) =>
      s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  // Regex (to match all types of tokens) to detect comments, strings, numbers, keywords, and operators
  const tokenRe = /~~[\s\S]*?~~|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\b\d+(\.\d+)?\b|\b[A-Za-z_][A-Za-z0-9_]*\b|[=+\-*/{}();<>]{2,}|[=+\-*/{}();<>]|[\t ]+|\r?\n|./g;

  // Define all Spyce language keywords and store them in a Set for faster lookup
  const keywordSet = new Set(['AND', 'NOT', 'OR', 'bool', 'break', 'case', 'char', 'choose',
    'const', 'continue', 'default', 'elsewhen', 'false', 'float',
    'for', 'giveback', 'int', 'listen', 'make', 'null', 'otherwise', 
    'say', 'skip', 'spyce', 'string', 'true', 'void', 'when', 'while']); // Set for fast keyword lookup
    const tokens = input.match(tokenRe) || [];
    let out = "";


  // Iterate through each token to apply syntax highlighting
  for (let i = 0; i < tokens.length; i++) {
    const tok = tokens[i];

    //----- COMMENTS -----
    // Detect and highlight Spyce comments enclosed in ~~ ... ~~
    if (/^~~[\s\S]*?~~$/.test(tok)) {
      out += `<span class="comment">${escapeHtml(tok)}</span>`;
      continue;
    }

    //----- STRINGS -----
    // Highlight string literals enclosed in "..."
    if (/^"([^"\\]|\\.)*"$/.test(tok) || /^'([^'\\]|\\.)*'$/.test(tok)) {
      out += `<span class="string">${escapeHtml(tok)}</span>`;
      continue;
    }

    //----- NUMBERS -----
    // Highlight numbers
    if (/^\d+(\.\d+)?$/.test(tok)) {
      out += `<span class="number">${escapeHtml(tok)}</span>`;
      continue;
    }

    //----- OPERATORS -----
    // Multi-character same operators (like ==, ++, **) are invalid in Spyce → show as identifier (white)
    if (/^([=+\-*/{}();<>])\1+$/.test(tok)) {
      out += `<span class="identifier">${escapeHtml(tok)}</span>`;
      continue;
    }

    //----- OPERATORS -----
    // Single-character valid operators → highlight in orange
    if (/^[=+\-*/{}();<>]$/.test(tok)) {
      out += `<span class="operator">${escapeHtml(tok)}</span>`;
      continue;
    }

    // ----- KEYWORDS AND IDENTIFIERS -----
    // Highlight reserved keywords; all other valid identifiers remain default white
    if (/^[A-Za-z_][A-Za-z0-9_]*$/.test(tok)) {
      if (keywordSet.has(tok)) {
        out += `<span class="keyword">${escapeHtml(tok)}</span>`;
      } else {
        out += escapeHtml(tok);   // regular variable/function name
      }
      continue;
    }

    // ----- DEFAULT -----
    // Everything else (invalid characters, unrecognized sequences) → keep white
    out += escapeHtml(tok);
  } 
  
  return out;
}

//----------------------------------------------
// Performs lexical analysis on the user’s input code.
const analyzeCode = () => {
  if (!socket || !socket.connected){
    setTerminalMsg('❌ Socket not connected');
    return;
  }

  if (code.trim() === ""){
    setTerminalMsg("⚠️ No input detected.")
    setTokens([]);
    return
  } 
  socket.emit('analyze_code', {code});
};

  // Get the total number of lines in the current code input
  const lineCount = code.split("\n").length;
//----------------------------------------------

  return (
    <main className={showLexical ? "lexical-open" : ""}>
      <div className="upper_container">

        {/* --- Top Control Buttons --- */}
        <div className="spyce" onClick={() => window.location.reload()}/>

        {/* Run Button (Triggers Lexical Analysis) */}
        <div className="runbtn" onClick={analyzeCode}>
          <FontAwesomeIcon 
            icon={faPlay} 
            style={{ marginRight: "8px" }} 
            />
            Run
        </div>

        {/* Placeholder for display or status elements */}
        <div className="display"></div>

        {/* Toggle Button to Show/Hide Lexical Table */}
        <div className="lexical" onClick={() => {handleLexicalClick(); analyzeCode();}}>
          Lexical
        </div>
      </div>
      <div className="codeAndTerminal">
        {/* --- Code Area/Editor Section --- */}
        <div className={`mid_container ${showLexical ? "shrink" : "expand"}`}>
          <div className="code-area-img-cont">

            {/* Line Number Column */}
            <div className="line_numbers">
              {Array.from({ length: lineCount }, (_, i) => (
                <div key={i}>{i + 1}</div>
              ))}
            </div>

            {/* Vertical Divider Line */}
            <div className="vline"></div>

            {/* Code Editing Area (Wrapper for Highlighted and Editable Layers) */}
            <div className="code-area-wrapper">

            {/* Highlighted Code (Read-only visual layer for syntax coloring) */}
              <pre
                id="highlightedCode"
                className="highlighted-code"
                dangerouslySetInnerHTML={{
                  __html: highlightCode(code.endsWith("\n") ? code + " " : code)
                }}
              ></pre>

              {/* Editable Textarea (User input layer for writing code) */}       
              <textarea
                id="codeInput" 
                className="code_input"
                placeholder="Type your code here..."
                spellCheck="false" // ✅ ADD (prevents red underline)
                value={code}
                onChange={(e) => setCode(e.target.value)}
                onScroll={(e) => {
                  const textArea = e.target as HTMLTextAreaElement;
                  const lineNumbers = document.querySelector(".line_numbers") as HTMLElement;
                  if (lineNumbers) {
                    lineNumbers.scrollTop = textArea.scrollTop;
                  }
                  const highlight = document.querySelector(".highlighted-code") as HTMLElement;
                  if (highlight) {
                    highlight.scrollTop = textArea.scrollTop;     // sync scroll
                    highlight.scrollLeft = textArea.scrollLeft;   // synchronize horizontal scroll
                  }
                }}
              />
            </div>
          </div>
        </div>

        {/* --- Lexical Analysis Table --- */}      
        <div className={`lexical_container ${showLexical ? "show" : "hide"}`}>
          <div className="lexical-cont">
            <table className="lexical_table">
              <thead>
                <tr>
                  <th>LEXEME</th>
                  <th>TOKEN</th>
                </tr>
              </thead>
              <tbody>
                {tokens.length > 0 ? (
                  tokens.map((t, index) => (
                    <tr key={index}>
                      <td>{t.lexeme}</td>
                      <td>{t.token}</td>
                    </tr>
                  ))
                ) : (
                  <tr>
                    <td colSpan={2} style={{ color: "#aaa" }}>
                      No tokens generated yet.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>

        {/* --- Terminal Section (Displays program output or status) --- */}
        <div className={`terminal ${showLexical ? "shrink" : "expand"}`}>
          <div className="terminal-word">TERMINAL</div>
          <div className="terminal-img-cont">
            <hr className="line" />
            <div className="terminal_text">{terminalMsg}</div>
          </div>
        </div>
      </div>
    </main>
  );
}

export default App;