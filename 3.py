import csv


def load_data(file_path):
    with open(file_path, 'r') as file:
        data = [row for row in csv.reader(file)]
    return data

def candidate_elimination(examples):
    specific_h = examples[0][:-1]  # Initialize the most specific hypothesis
    general_h = [['?' for _ in range(len(specific_h))] for _ in range(len(specific_h))]  # Initialize the most general hypothesis

    print("Step 0:")
    print("Specific Hypothesis (S0):", specific_h)
    print("General Hypothesis (G0):", general_h)

    for idx, example in enumerate(examples, start=1):
        if example[-1] == 'Y':  # For positive examples
            for i in range(len(specific_h)):
                if example[i] != specific_h[i]:
                    specific_h[i] = '?'  # Update specific hypothesis
                    general_h[i][i] = '?'  # Update general hypothesis

        else:  # For negative examples
            for i in range(len(specific_h)):
                if example[i] != specific_h[i]:
                    general_h[i][i] = specific_h[i]  # Update general hypothesis
                else:
                    general_h[i][i] = '?'  # Wildcard in case generalization is needed

        print(f"\nStep {idx}:")
        print("Specific Hypothesis (S{}):".format(idx), specific_h)
        print("General Hypothesis (G{}):".format(idx), general_h)

    # Refine the general hypotheses
    refined_general_h = []
    for hypothesis in general_h:
        if hypothesis not in refined_general_h:
            refined_general_h.append(hypothesis)

    return specific_h, refined_general_h

data = load_data('3.csv')
specific_hypothesis, general_hypotheses = candidate_elimination(data)

print("\nFinal Specific Hypothesis:", specific_hypothesis)
print("Final General Hypotheses:")
for hypothesis in general_hypotheses:
    print(hypothesis)
