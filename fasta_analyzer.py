from Bio import SeqIO
def count_sequence(filename):
    """Return the total number of sequences in FASTA file."""
    count=0
    for record in SeqIO.parse(filename,'fasta'):
        count+=1

    return count


def longest_sequence(filename):
    longest=0
    longest_id=''
    for record in SeqIO.parse(filename,'fasta'):
        length=len(record.seq)
        if length>longest:
            longest=length
            longest_id=record.id
    return longest_id,longest


def shortest_sequence(filename):
    shortest=None
    shortest_id=''
    for record in SeqIO.parse(filename,'fasta'):
        length=len(record.seq)
        if shortest is None or length<shortest:
            shortest=length
            shortest_id=record.id
    return shortest_id,shortest



def highest_gc(filename):
    highest=0
    high_gc_id=''
    for record in SeqIO.parse(filename,'fasta'):
        gc_percent=(record.seq.count('G')+record.seq.count('C'))/len(record.seq)*100
        if gc_percent>highest:
            highest=gc_percent
            high_gc_id=record.id
    return high_gc_id,highest


def lowest_gc(filename):
    lowest=None
    low_gc_id=''
    for record in SeqIO.parse(filename,'fasta'):
        gc_percent=(record.seq.count('G')+record.seq.count('C'))/len(record.seq)*100
        if lowest is None or gc_percent<lowest:
            lowest=gc_percent
            low_gc_id=record.id
    return low_gc_id,lowest


def average_length(filename):
    count_seq=0
    total=0
    for record in SeqIO.parse(filename,'fasta'):
        length=len(record.seq)
        total+=length
        count_seq+=1
    average=total/count_seq
    return average



def fasta_summary(filename):

    count=count_sequence(filename)

    longest_id,longest=longest_sequence(filename)

    shortest_id,shortest=shortest_sequence(filename)

    high_gc_id,highest=highest_gc(filename)

    low_gc_id,lowest=lowest_gc(filename)

    average=average_length(filename)

    summary={
        'total_sequence':count,
        'longest_id':longest_id,
        'longest_length':longest,
        'shortest_id':shortest_id,
        'shortest_length':shortest,
        'highest_gc_id':high_gc_id,
        'highest_gc':highest,
        'lowest_gc_id':low_gc_id,
        'lowest_gc':lowest,
        'average_length':average
    }

    return summary



def main():
    filename = input('Enter FASTA Filename:')
    try:
        summary = fasta_summary(filename)

    except FileNotFoundError:
        print(f"Error: '{filename}' was not found")
        print('Please check the filename and try again')
        return

    print("=" * 40)
    print("       FASTA ANALYZER")
    print("=" * 40)

    print()

    print(f"File Name             : {filename}")

    print()

    print(f"Total Sequences       : {summary['total_sequence']}")
    print()

    print(f"Longest ID            : {summary['longest_id']}")
   

    print(f"Longest Length        : {summary['longest_length']} bp")
    print()

    print(f"Shortest ID           : {summary['shortest_id']}")
    

    print(f"Shortest Length       : {summary['shortest_length']} bp")
    print()

    print(f"Highest GC ID         : {summary['highest_gc_id']}")
    

    print(f"Highest GC Percentage : {summary['highest_gc']:.2f}%")
    print()

    print(f"Lowest GC ID          : {summary['lowest_gc_id']}")
   

    print(f"Lowest GC Percentage  : {summary['lowest_gc']:.2f}%")
    print()

    print(f"Average Length        : {summary['average_length']:.2f} bp")
    
    print()
    print("=" * 40)
main()







