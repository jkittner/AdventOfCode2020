require(data.table)

find_sum_to_2020 <- function(exp_rep) {
    for (i in exp_rep) {
        for (j in exp_rep) {
            for (k in exp_rep) {
                val = i + j + k
                if (val == 2020) {
                    multip_var = i * j * k
                    return(multip_var)
                }
            }
        }
    }
}

main <- function() {
    data = fread('input.txt')
    solution = find_sum_to_2020(data$V1)
    cat(paste('the solution is:', solution))
}

main()
