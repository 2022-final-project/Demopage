import glob

using_sql_word = ['select', 'from', 'where', 'order', 'group', 'by'
                , 'limit', 'when', 'then', 'case', 'having'
                , 'sum', 'avg', 'min', 'max', 'count', 'in', 'exists', 'like'
                , 'and', 'or', 'not'
                , 'date', 'month', 'year', 'asc', 'desc', 'on', 'end', 'if', 'else']
aggregate_words = ['sum', 'avg', 'min', 'max', 'count']
refining_target = [',', '(', ')', '\'']
alias_dic = {}
table_dic = {}
column_dic = {}

def table_column_preprocessing(self):
        q = open('./sql_queries/temp/refined_test_queries2.txt', 'r')
        w = open('./modeling/test_data.txt', 'w')

        while True:
            line = q.readline()

            if line == "": break

            line = line.strip()
            word_list = line.split()

            for idx, word in enumerate(word_list):
                word = word.lower()
                if word in table_dic:               # table info preprocessing
                    word = table_dic[word]
                elif word in column_dic:            # column info preprocessing
                    word = column_dic[word]
                elif word not in using_sql_word:    # not using sql word remove
                    word = ''

                if word == '': continue
                w.write(word + ' ')
            w.write('\n')