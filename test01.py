
import seaborn as sns
import matplotlib.pyplot as plt
class AH:


    # fig, axs = plt.subplots(3, 4, sharex=True, sharey=True)
    fig, axs = plt.subplots(3, 4, sharex=True)

    keyS = ['atS', 'taS', 'tbS', 'trS', 'rtS', 'btS', 'raS', 'arS', 'rbS', 'brS', 'abS', 'baS']
    k = 0
    for i in range(3):
        for j in range(4):
            axs[i,j].set_xticks([8,7,6,5,4])
            sns.regplot(ax=axs[i, j], x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], y=[1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,16,130])
            # sns.regplot(ax=axs[i, j], x=[1,2,3,4,5], y=[2,3,4,5,5])
           # axs[i,j].set_title(keyS[k])
            axs[i,j].set_xticks([0,5,10,15,20,25,30])
            axs[i,j].set_yticks([0,20,40,60,80,100,120])

            k += 1

    # Set common labels
    fig.supxlabel('simple count')
    fig.supylabel('consuming times by block timestamp(cross chain)')

    plt.tight_layout()
    plt.show()