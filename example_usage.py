from client import CodebaseSemanticAstSymbolIndexerContextClient

def main():
    client = CodebaseSemanticAstSymbolIndexerContextClient()
    res = client.build_codebase_context_window('server/api/payment.py', 'process_refund')
    print('Index Session: ' + res['index_session_id'] + ' for symbol: ' + res['queried_symbol'])
    print('Resolved AST Nodes: ' + ', '.join(res['resolved_ast_definitions']))
    print('Context Tokens: ' + str(res['inline_ai_edit_context_tokens']) + ' | Speculative Diff: ' + str(res['multi_file_speculative_diff_ready']))

if __name__ == '__main__':
    main()
