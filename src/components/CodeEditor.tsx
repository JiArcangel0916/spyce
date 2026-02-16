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

    monaco.languages.setMonarchTokensProvider('spyce', {
      keywords: ['AND', 'NOT', 'OR', 'bool', 'break', 'case', 'char', 'choose',
        'const', 'continue', 'default', 'elsewhen', 'false', 'float',
        'for', 'giveback', 'int', 'listen', 'make', 'otherwise', 'say',
        'skip', 'spyce', 'str', 'string', 'true', 'void', 'when', 'while'],
      tokenizer: {
        root: [
          [/~~[\s\S]*?~~/, 'comment'],    // comments
          [/[A-Za-z_][A-Za-z0-9_]*/, {    // keyowrds and idenfitiers
            cases: {
              '@keywords': 'keyword',
              '@default': 'identifier'
            }
          }],

          [/"(?:\\.|[^"\\])*"/, "string"], // string and char
          [/'(?:\\.|[^'\\])*'/, "string"],

          [/\d+(\.\d+)?/, "number"],

          [/[=+\-*/{}();<>]/, "operator"],
          [/->/, "operator"],
        ]
      }
    });

    monaco.editor.defineTheme('spyceTheme', {
      base: 'vs-dark',
      inherit: true,
      rules: [
        { token: 'keyword', foreground: 'FFD700', fontStyle: 'bold' },
        { token: 'identifier', foreground: 'F3DFDF' },
        { token: 'string', foreground: '3FF33F' },
        { token: 'comment', foreground: 'A3A3A3', fontStyle: 'italic' },
        { token: 'number', foreground: 'E13998' },
        { token: 'operator', foreground: 'DF7852' },
      ],
      colors: {
        'editor.background': '#00000000',
        'editorLineNumber.foreground': '#FFFFFF',
        'editorCursor.foreground': '#FFFFFF',
        'editorLineNumber.activeForeground':'#FFFFFF',
        'editorLineHighlightBackground': '#FFFFFF',
        'editor.lineHighlightBorder':'#ffffff7a'
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
          {
            label: 'spyce',
            kind: monaco.languages.CompletionItemKind.Snippet,
            insertText: 'spyce() -> void {\n\tgiveback void;\n}',
            documentation: 'Main function in SPyCe',
            range: range,
          } // add keyword suggestion here
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