class CodebaseSemanticAstSymbolIndexerContextClient:
    def build_codebase_context_window(self, active_file='src/core/router.py', query_symbol='dispatch_request', max_context_tokens=8192):
        return {
            'index_session_id': 'csr_ast_9918',
            'target_file': active_file,
            'queried_symbol': query_symbol,
            'resolved_ast_definitions': ['src/core/router.py:45 (def dispatch_request)', 'src/middleware/auth.py:12 (class AuthMiddleware)'],
            'semantic_file_embeddings_retrieved': 5,
            'inline_ai_edit_context_tokens': 3450,
            'type_inference_callgraph_resolved': True,
            'multi_file_speculative_diff_ready': True
        }
