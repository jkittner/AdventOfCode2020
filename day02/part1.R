library(data.table)
library(tidyr)
library(stringr)


valid_pw <- function(min_nr, max_nr, letter, pw_str) {
    letter_count <- str_count(string = pw_str, pattern = letter)
    if (letter_count >= min_nr && letter_count <= max_nr) {
        return(TRUE)
    } else {
        return(FALSE)
    }
}

main <- function() {
    data <- fread(input='input.txt', header = F, sep = ':')
    colnames(data)[2] <- 'pw_str'
    data_seperate <- separate(
        data=data,
        col = V1,
        into = c('min_nr', 'max_nr', 'letter'),
        sep='[\\s]|[-]'
    )# fix types
    data_seperate[, min_nr := as.numeric(min_nr)]
    data_seperate[, max_nr := as.numeric(max_nr)]
    data_seperate[,is_valid := valid_pw(min_nr, max_nr, letter, pw_str),
                  by = seq_len(nrow(data_seperate))]
    nr_valid_pw <- sum(data_seperate$is_valid)
    print(paste('the solution is:', nr_valid_pw))
}

main()
