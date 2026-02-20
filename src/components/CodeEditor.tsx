import React from 'react';
import Editor, { OnMount } from '@monaco-editor/react';
import '../styles/CodeEditor.css';

interface CodeEditorProps {
  code: string;
  setCode: (val: string) => void;
  showLexical: boolean;
}

export const CodeEditor: React.FC<CodeEditorProps> = ({ code, setCode, showLexical }) => {
  const handleEditorOnMount: OnMount = (editor, monaco) => {
    monaco.languages.register({ id: 'spyce' })

    monaco.languages.setLanguageConfiguration('spyce', {
      brackets: [
        ['{', '}'],
        ['[', ']'],
        ['(', ')'],
      ],
      autoClosingPairs: [
        { open: '{', close: '}' },
        { open: '[', close: ']' },
        { open: '(', close: ')' },
        { open: '"', close: '"' },
        { open: "'", close: "'" },
        { open: '~~', close: '~~' },
      ],
      surroundingPairs: [
        { open: '{', close: '}' },
        { open: '[', close: ']' },
        { open: '(', close: ')' },
        { open: '"', close: '"' },
        { open: "'", close: "'" },
      ],
    });

    monaco.languages.setMonarchTokensProvider('spyce', {
      keywords:     ['break', 'const', 'continue', 'false', 'listen', 'say', 'skip', 'spyce', 'str', 'giveback', 'true', 'false'],
      datatypes:    ['int', 'float', 'char', 'string', 'bool'],
      logops:       ['AND', 'OR', 'NOT'],
      ctrlstructs:  ['for', 'while', 'when', 'elsewhen', 'otherwise', 'choose', 'case', 'default'],
      tokenizer: {
        root: [
          // comments
          [/~~[\s\S]*?~~/, 'comment'],    

          // keyowrds and idenfitiers
          [/[A-Za-z_][A-Za-z0-9_]*/, {    
            cases: {
              '@keywords'     : 'keyword',
              '@datatypes'    : 'datatype',
              '@logops'       : 'logop',
              '@ctrlstructs'  : 'ctrlstruct',
              'make'          : 'make',
              'void'          : 'void',
              '@default'      : 'identifier'
            }
          }],

          // string and char
          [/"(?:\\.|[^"\\])*"/, "string"], 
          [/'(?:\\.|[^'\\])*'/, "string"],

          // numbers
          [/\d+(\.\d+)?/, "number"],

          // operators
          [/[=+\-*/{}();<>]/, "operator"],
          [/->/, "operator"],
        ]
      }
    });

    monaco.editor.defineTheme('spyceTheme', {
      base: 'vs-dark',
      inherit: true,
      rules: [
        { token: 'keyword', foreground: 'FFD700' },
        { token: 'identifier', foreground: 'F3DFDF' },
        { token: 'string', foreground: '3FF33F' },
        { token: 'comment', foreground: 'A3A3A3', fontStyle: 'italic' },
        { token: 'number', foreground: 'E13998' },
        { token: 'operator', foreground: 'DF7852' },
        { token: 'datatype', foreground: '67BED9' },
        { token: 'logop', foreground: 'a2d827' },
        { token: 'ctrlstruct', foreground: 'ff00fa' },
        { token: 'make', foreground: 'FF7700' },
        { token: 'void', foreground: '509faf' }

      ],
      colors: {
        'editor.background': '#000000',
        'editorLineNumber.foreground': '#FFFFFF',
        'editorCursor.foreground': '#FFFFFF',
        'editorLineNumber.activeForeground': '#FFFFFF',
        'editorLineHighlightBackground': '#FFFFFF',
        'editor.lineHighlightBorder': '#ffffff7a'
      }
    });

    monaco.languages.registerCompletionItemProvider('spyce', {
      provideCompletionItems: (model, position) => {
        const word = model.getWordUntilPosition(position);
        const range = {
          startLineNumber: position.lineNumber,
          endLineNumber: position.lineNumber,
          startColumn: word.startColumn,
          endColumn: word.endColumn,
        };

        const suggestions = [
          // SPYCE FUNCTION SNIPPET
          {label: 'spyce (spy)', kind: monaco.languages.CompletionItemKind.Snippet, insertText: 'spyce() -> void {\n\tgiveback void;\n}', documentation: 'Main function in SPyCe', range: range},
          
          // DATA TYPES AND VARIABLES
          {label: 'int (int)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'int', documentation: 'Represents an integer data type', range: range},
          {label: 'float (flo)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'float', documentation: 'Represents a float data type', range: range},
          {label: 'char (char)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'char', documentation: 'Represents a character data type', range: range},
          {label: 'string (str)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'string', documentation: 'Represents a string data type', range: range},
          {label: 'bool (boo)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'bool', documentation: 'Represents a boolean type', range: range},
          
          // IO
          {label: 'say (say)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'say();', documentation: 'Outputs text, variables, or results to the screen', range: range},
          {label: 'listen (lis)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'listen()', documentation: 'Used to accept user input', range: range},

          // LOGICAL OPERATORS
          {label: 'AND (and)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'AND', documentation: 'Returns true only if both operands are true', range: range},
          {label: 'OR (or)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'OR', documentation: 'Returns true if at least one operand is true', range: range},
          {label: 'NOT (not)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'NOT', documentation: 'Reverses the truth value', range: range},

          // CONDITIONALS
          {label: 'when (whe)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'when(){\n\n}', documentation: 'Executes a block of code if a certain condition is true', range: range},
          {label: 'elsewhen (els)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'elsewhen(){\n\n}', documentation: 'Executes a block of code if a previous conditional was false and this condition is true', range: range},
          {label: 'otherwise (oth)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'otherwise{\n\n}', documentation: 'Executes when no previous conditions were true', range: range},
          {label: 'choose (cho)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'choose(){\n\n}', documentation: 'Used to select one of many code blocks to be executed', range: range},
          {label: 'case (cas)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'case', documentation: 'Defines a specific case inside a choose conditional', range: range},
          {label: 'default (def)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'default:\n', documentation: 'Fallback if no other case matches', range: range},

          // ITERATION
          {label: 'for (for)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'for(){\n\n}', documentation: 'Loops over a range, sequence,  or iterable', range: range},
          {label: 'while (whi)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'while(){\n\n}', documentation: 'Fallback if no other case matches', range: range},
          {label: 'break (bre)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'break', documentation: 'Exits immediately', range: range},
          {label: 'skip (ski)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'skip', documentation: 'Does nothing; a placeholder statement for blocks that does not allow empty definitions', range: range},
          {label: 'continue (con)' , kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'continue', documentation: 'Skips current iteration and goes to the next loop cycle', range: range},

          // OTHERS
          {label: 'true (tru)', kind: monaco.languages.CompletionItemKind.Value, insertText: 'true', documentation: 'Boolean literal for truth', range: range},
          {label: 'false (fal)', kind: monaco.languages.CompletionItemKind.Value, insertText: 'false', documentation: 'Boolean literal for falsehood', range: range},
          {label: 'make (mak)', kind: monaco.languages.CompletionItemKind.Function, insertText: 'make', documentation: 'Defines a function', range: range},
          {label: 'const (con)', kind: monaco.languages.CompletionItemKind.Constant, insertText: 'const', documentation: 'Declares a constant variable', range: range},
          {label: 'void (voi)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'void', documentation: 'Indicates no return value from a function', range: range},
          {label: 'giveback (giv)', kind: monaco.languages.CompletionItemKind.Keyword, insertText: 'giveback', documentation: 'Ends a function and sends a value back to where the function was called', range: range},
          {label: 'str (str)', kind: monaco.languages.CompletionItemKind.Method, insertText: 'str()', documentation: 'Converts its arguments to string', range: range},  
        ];
        return { suggestions };
      }
    });

    monaco.editor.setTheme('spyceTheme');
  };

  return (
    <div className="codeWrapper">
      <Editor
        height='100%'
        language='spyce'
        theme='spyceTheme'
        value={code}
        onMount={handleEditorOnMount}
        onChange={(val) => setCode(val || "")}
        options={{
          fontSize: 20,
          fontFamily: "'Fira Code', monospace",
          minimap: { enabled: false },
          automaticLayout: true,
          fixedOverflowWidgets: true,
          lineNumbers: "on",
          scrollBeyondLastLine: false,
          renderLineHighlight: "all",
          lineDecorationsWidth: 10
        }}
      />
    </div>
  )
}