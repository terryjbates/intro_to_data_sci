import csv
import sys

def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the 
    Instructor Notes below for more details on the task. 
    
    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        output_file = "updated_" + name
        output_file_fd = open(output_file, 'wb')
        writer = csv.writer(output_file_fd, lineterminator='\n')

        input_file = open(name, 'rb')
        reader = csv.reader(input_file)

        for row in reader:
            row_prefix = row[:3]
            row_tail = row[3:]

            # Strip surrounding whitespace chars from all row_tail elements
            for x in xrange(len(row_tail)):
                row_tail[x] = row_tail[x].strip()
            
            row_tail_len = len(row_tail)
            div = 5
            recs = row_tail_len / div
            min = 0
            max = 5
            
            while max < row_tail_len:
                #print list(row_prefix) + row_tail[min:max]
                row_record = list(row_prefix) + row_tail[min:max]
                # Sanity check row record
                #print row_record      
                writer.writerow(row_record)
                max += 5
                min = max -5
                
        input_file.close()  
        output_file_fd.close()

def main():
    print sys.version
    filenames = ['head_20_turnstile_110507.txt']
    fix_turnstile_data(filenames)
    
    
if __name__ == "__main__":
    main()

