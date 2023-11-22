import re
import difflib

def extract_text_inside_brackets(text):
    return re.findall(r'\[(.*?)\]', text, re.DOTALL)

def EvaluateDecompiler(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()

            sections1 = extract_text_inside_brackets(content1)
            sections2 = extract_text_inside_brackets(content2)

            total_similarity = 0
            num_sections = min(len(sections1), len(sections2))

            for i in range(num_sections):
                section1 = sections1[i].strip()
                section2 = sections2[i].strip()

                similarity = difflib.SequenceMatcher(None, section1, section2).ratio()
                similarity_percentage = similarity * 100

                print(f"Similarity for section {i + 1}: {similarity_percentage:.2f}%")
                print(f"Section {i + 1}:\n{section1}\n")

                diff = difflib.unified_diff(section1.splitlines(), section2.splitlines(), fromfile=file1, tofile=file2, lineterm="")
                diff_text = '\n'.join(diff)
                if diff_text:
                    print(f"Differences for section {i + 1}:\n{diff_text}\n")
                else:
                    print(f"No differences found for section {i + 1}.\n")

                total_similarity += similarity_percentage

            overall_similarity = total_similarity / num_sections if num_sections > 0 else 0
            print(f"Overall Similarity: {overall_similarity:.2f}%")

            return overall_similarity
    except IOError as e:
        print(f"An error occurred while reading the files: {e}")
        return 0

# Test with your example files
TestInputFile = "/Users/karl-emilkensmark/Documents/GitHub/Program-Analysis/projekt/ressources/java_files/output_files/EvalVar1.java"
TestOutputFile = "/Users/karl-emilkensmark/Documents/GitHub/Program-Analysis/projekt/ressources/java_files/output_files/EvalVar2.java"
EvaluateDecompiler(TestInputFile, TestOutputFile)
