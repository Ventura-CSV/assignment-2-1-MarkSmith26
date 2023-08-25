def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    males = input('Please enter number of males: ')
    females = input('Please enter number of females: ')
    total_stu = int(males) + int(females)
    m_perc = (int(males) / int(total_stu)) * 100
    f_perc = (int(females) / int(total_stu)) * 100

    print(f'The total number of students: \t {total_stu}')
    print(f'The number of males and females: \t {int(males)} \t {int(females)}')
    print(f'The percentage of males and females: \t {m_perc} \t {f_perc}') 

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
