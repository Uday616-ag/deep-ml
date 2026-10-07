import numpy as np

def calculate_latency_percentiles(latencies: list[float]) -> dict[str, float]:
    """
    Calculate P50, P95, and P99 latency percentiles.
    
    Args:
        latencies: List of latency measurements
    
    Returns:
        Dictionary with keys 'P50', 'P95', 'P99' containing
        the respective percentile values rounded to 4 decimal places
    """
    latencies=np.array(latencies)
    lenght=latencies.size

    
    if lenght==0:
        return {'P50':0,
            'P95':0,
            'P99':0}
 
    p50=np.round(np.percentile(latencies,50),4)
    p95=np.round(np.percentile(latencies,95),4)
    p99=np.round(np.percentile(latencies,99),4)
    

    if lenght==0:
        return 0
        
    return {'P50':p50,
            'P95':p95,
            'P99':p99}