import React from 'react';
import "../styles/Terminal.css";

interface TerminalProps {
    message: string;
    showLexical: boolean;
}

export const Terminal: React.FC<TerminalProps> = ({ message, showLexical }) => {
    return (
        <div className={`terminal ${showLexical ? "shrink" : "expand"}`}>
          <div className="terminal-img-cont">
            <div className="terminal-word">TERMINAL</div>  
            <hr className="line" />
            <div className="terminal-text">{message}</div>
          </div>
        </div>
    )
}