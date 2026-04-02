import { faPlay } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import "../styles/Header.css";
import logo from "../assets/spyce.png";

interface HeaderProps {
    openFile: () => void;
    saveFile: () => void;
    onRun: () => void;
    onLexical: () => void;
    onSyntax: () => void;
    onSemantic: () => void;
}

export const Header: React.FC<HeaderProps> =({ openFile, saveFile, onRun, onLexical, onSyntax, onSemantic }) => {
    return(
        <div className="mainHeader">
            <div className="leftBtns">
                {/* <div className="spyce" onClick={() => window.location.reload()}/> */}
                <img src={logo} className="spyce" onClick={() => window.location.reload()} />
                <div className="open" onClick={openFile}>Open</div>
                <div className="save" onClick={saveFile}>Save</div>
                <div className="runBtn" onClick={onRun}>
                    <FontAwesomeIcon icon={ faPlay } />
                    Run
                </div>
            </div>

            <div className="rightBtns">
                <div className="lexicalBtn" onClick={onLexical}>Lexical</div>
                <div className="syntaxBtn" onClick={onSyntax}>Syntax</div>
                <div className="semanticBtn" onClick={onSemantic}>Semantic</div>
            </div>
        </div>
    )
}