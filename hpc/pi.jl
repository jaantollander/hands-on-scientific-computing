n = 100
success = sum(rand(n).^2 + rand(n).^2 .<= 1)
print("{\"pi_estimate\": $(4*success/n), \"iterations\": $(n), \"successes\": $(success)}")
