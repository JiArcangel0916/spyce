import { faPlay } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import "../styles/Header.css";

interface HeaderProps {
    onRun: () => void;
    onLexical: () => void;
    onSyntax: () => void;
}

export const Header: React.FC<HeaderProps> =({ onRun, onLexical, onSyntax }) => {
    return(
        <div className="mainHeader">
            <div className="leftBtns">
                <div className="spyce" onClick={() => window.location.reload()}/>
                <div className="runBtn" onClick={onRun}>
                    <FontAwesomeIcon icon={ faPlay } />
                    Run
                </div>
            </div>

            <div className="rightBtns">
                <div className="lexicalBtn" onClick={onLexical}>Lexical</div>
                <div className="syntaxBtn" onClick={onSyntax}>Syntax</div>
            </div>
        </div>
    )
}