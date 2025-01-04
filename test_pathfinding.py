from pathfinding import PathFinding, compare_algorithms

def create_test_grids():
    """sample sparse and dense grids for testing"""
    sparse_grid = [
        ['S', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', 'X', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', 'X', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'X', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'G']
    ]

    dense_grid = [
        ['S', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'],
        ['.', 'X', '.', 'X', '.', 'X', '.', 'X', '.', 'X'],
        ['X', '.', 'X', '.', '.', '.', 'X', '.', 'X', '.'],
        ['.', 'X', '.', 'X', 'X', 'X', '.', 'X', '.', 'X'],
        ['X', '.', '.', 'X', '.', '.', '.', '.', 'X', '.'],
        ['.', 'X', '.', '.', '.', 'X', 'X', '.', '.', 'X'],
        ['X', '.', 'X', 'X', '.', 'X', '.', 'X', '.', '.'],
        ['.', 'X', '.', '.', 'X', '.', '.', '.', 'X', '.'],
        ['X', '.', 'X', '.', '.', 'X', '.', 'X', '.', 'X'],
        ['.', 'X', '.', 'X', '.', '.', 'X', '.', '.', 'G']
    ]

    return sparse_grid, dense_grid

def print_analysis_results(grid_type, results):
    """print formatted analysis results"""
    print(f"\n=== {grid_type} Grid Analysis ===")
    
    for algo, metrics in results.items():
        print(f"\nAlgorithm: {algo}")
        if isinstance(metrics, dict) and 'manhattan' in metrics:
            # A* results with different heuristics
            for heuristic, h_metrics in metrics.items():
                print(f"\n  Heuristic: {heuristic}")
                print(f"    Time: {h_metrics['execution_time']:.4f}s")
                print(f"    Memory: {h_metrics['memory_usage']:.2f}MB")
                print(f"    Nodes expanded: {h_metrics['nodes_expanded']}")
        else:
            # BFS/DFS results
            print(f"  Time: {metrics['execution_time']:.4f}s")
            print(f"  Memory: {metrics['memory_usage']:.2f}MB")
            print(f"  Nodes expanded: {metrics['nodes_expanded']}")

def compare_efficiency(sparse_results, dense_results):
    """compare and print efficiency ratios between dense and sparse grids"""
    print("\n=== Efficiency Comparison (Dense vs Sparse) ===")
    for algo in sparse_results.keys():
        if algo == 'astar':
            for heuristic in sparse_results[algo].keys():
                sparse_efficiency = sparse_results[algo][heuristic]['nodes_expanded']
                dense_efficiency = dense_results[algo][heuristic]['nodes_expanded']
                ratio = dense_efficiency / sparse_efficiency
                print(f"\nA* ({heuristic}):")
                print(f"  Dense/Sparse node expansion ratio: {ratio:.2f}")
        else:
            sparse_efficiency = sparse_results[algo]['nodes_expanded']
            dense_efficiency = dense_results[algo]['nodes_expanded']
            ratio = dense_efficiency / sparse_efficiency
            print(f"\n{algo.upper()}:")
            print(f"  Dense/Sparse node expansion ratio: {ratio:.2f}")

def main():
    # create test grids
    sparse_grid, dense_grid = create_test_grids()

    # run analysis
    print("\nRunning performance analysis on Sparse Grid...")
    sparse_results = compare_algorithms(sparse_grid)

    # run analysis
    print("\nRunning performance analysis on Dense Grid...")
    dense_results = compare_algorithms(dense_grid)

    # print detailed results
    print_analysis_results("Sparse", sparse_results)
    print_analysis_results("Dense", dense_results)

    # compare efficiency ratios
    compare_efficiency(sparse_results, dense_results)

if __name__ == "__main__":
    main() 