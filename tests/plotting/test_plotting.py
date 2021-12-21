import os
import pytest
from spapros import pl


#############
# selection #
#############


def test_masked_dotplot(small_adata, selector):
    pl.masked_dotplot(small_adata, selector, save="tests/plotting/test_data/tmp_masked_dotplot.png")
    with open(f"tests/plotting/test_data/tmp_masked_dotplot.png", "rb") as file:
        plot = file.read()
    os.remove(f"tests/plotting/test_data/tmp_masked_dotplot.png")
    with open(f"tests/plotting/test_data/masked_dotplot.png", "rb") as file:
        ref_plot = file.read()
    assert plot == ref_plot


##############
# evaluation #
##############


def test_plot_summary(evaluator):
    ref_name = "tests/plotting/test_data/plot_summary.png"
    fig_name = "tests/plotting/test_data/tmp_plot_summary.png"
    evaluator.plot_summary(show=False, save=fig_name)
    with open(fig_name, "rb") as file:
        plot = file.read()
    os.remove(fig_name)
    with open(ref_name, "rb") as file:
        ref_plot = file.read()
    assert plot == ref_plot


@pytest.mark.parametrize("metric", ["gene_corr", "forest_clfs"])
def test_plot_evaluations_gene_corr(evaluator, small_probeset, metric):
    evaluator.evaluate_probeset(small_probeset)
    # evaluator.plot_evaluations(metrics=[metric], show=False,
    #                            save=f"tests/plotting/test_data/plot_evaluations_{metric}.png")
    evaluator.plot_evaluations(metrics=[metric], show=False,
                               save=f"tests/plotting/test_data/tmp_plot_evaluations_{metric}.png")
    with open(f"tests/plotting/test_data/tmp_plot_evaluations_{metric}.png", "rb") as file:
        plot = file.read()
    os.remove(f"tests/plotting/test_data/tmp_plot_evaluations_{metric}.png")
    with open(f"tests/plotting/test_data/plot_evaluations_{metric}.png", "rb") as file:
        ref_plot = file.read()
    assert plot == ref_plot
