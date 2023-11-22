import difflib

def tokenize_line(line):
    return line.split()

def EvaluateDecompiler(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

            total_word_count = 0
            total_match_count = 0

            for line1, line2 in zip(lines1, lines2):
                words1 = tokenize_line(line1)
                words2 = tokenize_line(line2)

                similarity = difflib.SequenceMatcher(None, words1, words2).ratio()
                similarity_percentage = similarity * 100

                print(f"Similarity for line:\n{line1}")
                print(f"vs.\n{line2}")
                print(f"Similarity: {similarity_percentage:.2f}%")

                total_word_count += max(len(words1), len(words2))
                total_match_count += int(similarity * min(len(words1), len(words2)))

            overall_similarity = (total_match_count / total_word_count) * 100 if total_word_count > 0 else 0
            print(f"Overall Similarity: {overall_similarity:.2f}%")

            return overall_similarity
    except IOError as e:
        print(f"An error occurred while reading the files: {e}")
        return 0

# Test with your example files
TestInputFile = "projekt/ressources/Evaluate1.java"
TestOutputFile = "projekt/ressources/Evaluate2.java"
EvaluateDecompiler(TestInputFile, TestOutputFile)
