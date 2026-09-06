Many aspects of brain function challenge the intuition of efficient information processing inherited from the fields of engineering and computer science
([Sarpeshkar, 1998](Sarpeshkar1998.pdf); [Edelman & Gally, 2001](Edelman2001.pdf); [Balasubramanian et al., 2001](Balasubramanian2001.pdf); [Faisal et al., 2008](Faisal2008.pdf); [Sterling & Laughlin, 2015](Sterling2015.pdf); [Sinz et al., 2019](Sinz2019.pdf); [Aimone & Parekh, 2023](Aimone2023.pdf); [Brette, 2026](Brette2026.pdf)).
In particular, the energetic perspective is likely the most striking of such counter-intuitive aspects ([Sterling & Laughlin, 2015](Sterling2015.pdf)).

Already in the early years of modern neuroscientific research, puzzling observations started to challenge our intuition.
In 1955, [Sokoloff and colleagues](Sokoloff1955.pdf) aimed at measuring the physiological and metabolic correlates of sustained mental effort.
In their study, mental effort was induced by asking participants to answer non-trivial arithmetic problems (reproduced in [Fig.a](../Figures/Sokoloff-1955.svg)).

%%beginFigure%%
![](../Figures/Sokoloff-1955.svg)   
**| Effect of mental effort on neural activity and cerebral oxygen consumption.** 
(a) Example arithmetic problems used to induce mental effort.
(b) Example electroencephalographic (EEG) activity patterns in control and mental arithmetic conditions.
(c) Measurements of Cerebral Metabolic Rate for Oxygen consumption ($\textnormal{CMR}_{O^2}$) in control (C) and mental effort (E) conditions across 13 subjects. Note the lack of significant changes between the two conditions.
Reproduced from [Sokoloff et al., 1955](Sokoloff1955.pdf).  
%%endFigure%%

Solving such problems with a modern artificial intelligence system (i.e. implementing the intuition derived from engineering and computer science) would involve spending a high amount of energy on this specific task.
Briefly, this task would be divided into two sub-problems.
First, a perceptual problem: recognising the digits and operators presented, which can be solved with a deep vision network (a CNN or a vision transformer).
The second sub-problem, the arithmetic itself, is computationally trivial once the operands are extracted: a handful of machine instructions will be executed by deterministic digital logic.
Considering very rough estimates, such a process would consume several kilowatts over a few seconds\footnote{ a frontier vision CNN running on Graphical Processing Units (GPUs), e.g. the DGX H100, see https://docs.nvidia.com/dgx/dgxh100-user-guide/, requires a power of around $\sim10^4$ Watts. }.
This considerable cost reflects a general property of artificial systems: reliability is achieved by operating at _a very high signal-to-noise ratio at every processing stage_ with large voltage changes, high-precision arithmetic units, and heavily over-parameterised networks trained to be robust to input variability ([Sarpeshkar, 1998](Sarpeshkar1998.pdf)).  

On the other hand, the measurements of [Sokoloff and colleagues](Sokoloff1955.pdf) led to a very different picture.
Their sustained mental effort task clearly induced modulations of brain activity associated with high cognitive loads (see [Fig.b](../Figures/Sokoloff-1955.svg), note the increase of high-frequency activity in electroencephalogram patterns).
In parallel, they estimated blood flow and oxygen consumption by collecting simultaneous samples of both arterial and venous blood and by leveraging the previously-introduced nitrous oxide method ([Kety & Schmidt, 1948](Kety1948.pdf)).
Contrary to their expectations, they could not find a significant difference in energy consumption between control and mental effort conditions (see [Fig.c](../Figures/Sokoloff-1955.svg)).
Therefore, despite clear changes in neural activity patterns ([Fig.b](../Figures/Sokoloff-1955.svg)), no significant changes in cerebral oxygen consumption could be observed during sustained mental effort ([Sokoloff et al., 1955](Sokoloff1955.pdf)).
This early study by Sokoloff and colleagues had several limitations. Notably, it measured only a global, whole-brain arteriovenous oxygen difference (it could not resolve regional changes), at a single time point, in a small cohort, and it captured strictly oxidative processes\footnote{
This picture has since been substantially refined. 
Three decades later, PET studies by Fox and Raichle (1986; 1988; reviewed in Fox and Raichle, 2007) showed that at the regional level, focal neural activation does produce a measurable rise in oxygen consumption, but one far smaller ($\sim5\%$) than the accompanying rises in cerebral blood flow (CBF) and glucose use ($\sim50\%$), revealing that much of the acute energetic response is met by non-oxidative (aerobic) glycolysis rather than oxidative phosphorylation. 
This same CBF/CMR$_{O^2}$ modulation is what BOLD fMRI exploits as its physiological basis, and calibrated fMRI approaches now allow this small residual CMR$_{O^2}$ change to be estimated quantitatively at the regional level. 
}.[](Fox1986.pdf) [](Fox1988.pdf) [](Fox2007.pdf)   
However, despite these limitations, their observation identified a core organisational principle of energy use: _the brain's total energy budget is dominated by a large, largely fixed baseline cost ($\sim$ 12 Watts), against which any task-evoked increment is rather marginal_. Later research has further detailed the biophysical machinery behind this principle (see [Attwell & Laughlin, 2001](Attwell2001.pdf); [Sterling & Laughlin, 2015](Sterling2015.pdf)).
The brain uses a computational strategy where incoming signals modulate the activity of synapses and neurons (themselves low-signal-to-noise, unreliable devices), and reliability is instead achieved statistically, through redundancy and population coding rather than through high per-unit fidelity ([Shadlen & Newsome, 1998](Shadlen1998.pdf), [Pouget et al., 2000](Pouget2000.pdf)).

Such findings thus lead to the general idea that **information processing in the brain is mostly performed by dynamical reorganisation of ongoing neural activity** rather than involving task-specific computations unfolding on an otherwise silent substrate.

Arousal-dependent modulations of cortical activity in the behaving mouse offer another striking illustration of this working principle, and one into which _in vivo_ neurophysiology has provided particularly deep insight.

%%beginFigure%%
![](../Figures/ephys-awake.svg) 
**| Example reconfiguration of neural dynamics during behavior in the mouse sensory cortex**.
**(a)** Schematic of the experimental setup to investigate visual processing during behavior in mice.
**(b)** A 30s recording sample showing a transition between an active and a quiet period. From top to bottom. 
Spiking activity (black) of *single units* isolated by spike sorting ([Pachitariu et al., 2024](Pachitariu2024.pdf)) and displayed as a raster plot (dots) and as a population firing rate (plain curve, smoothed with $T_{smooth}$=100ms).
Multi-Unit Activity (blue, *MUA*) computed as the smoothed ($T_{smooth}$=100ms) and rectified traces of the 0.3-3 kHz band-pass filtered raw electrophysiological recording and averaged over all recording electrodes.
Local Field Potentials (green, *LFP*) in 5 electrodes spanning the depth of the mouse primary visual cortex. 
Pupil size (red), estimated by fitting an ellipse to each frame; see insets for examples of pupil size at low and high dilation levels.
Whisking activity (purple, _whisking_) computed from the motion energy of the camera frames restricted to the whisker pad area.
Running traces (blue, _running_) computed from the rotations of the linear treadmill.
**(c)** Same as **b** but zoomed on a 2s active period. The smoothing time constant was now lowered to $T_{smooth}$=10ms.
**(d)** Same as **c** but zoomed on a 2s quiescent period.
Unpublished data from Zhang, Rebola & Zerlaut.
%%endFigure%%

[Fig.a](../Figures/ephys-awake.svg) shows a schematic of our experimental setup implementing such neurophysiological and behavioural recordings. 
Mice are head-fixed and positioned on a linear treadmill, free to run, in front of two V-shaped LED screens while a camera tracks pupil dilation and whisking activity. 
After $\sim$ 10 days of gradual habituation to the recording conditions, mice display spontaneous transitions between quiet and active periods (see a transition example in [Fig.b](../Figures/ephys-awake.svg)).
Active periods consist of transient epochs characterised by locomotor and whisking activity and are associated with a dilated pupil.
Such periods last from a few seconds to a minute or two and are interleaved with generally longer periods of quiescence.
This experimental rig is complemented with high-density electrophysiological 
recordings (using *Neuropixels* silicon probes, [Jun et al., 2017](Jun2017b.pdf)) to record the neural activity of $\sim$ 50-100 (spike-sorted) single units together with population signals such as Local Field Potentials (LFPs) and Multi-Unit Activity (MUA) in the primary visual cortex (V1) of the mouse.

During periods of high arousal (i.e. associated with locomotion, whisking and pupil dilation, highlighted in [Fig.c](../Figures/ephys-awake.svg)), neural activity is characterised by irregular, temporally decorrelated ("desynchronised") spiking. By contrast, during periods of quiescence and low arousal (highlighted in [Fig.d](../Figures/ephys-awake.svg)), neural activity can display slow, rhythmic, and highly correlated fluctuations in the $\sim$ 3-5Hz low-frequency range.

Interestingly, low-arousal activity does not show quiescent or negligible ongoing activity; rather, it displays very comparable levels of average spiking activity compared to the active period (note the similar average values of the firing rate and MUA after strong temporal smoothing in [Fig.b](../Figures/ephys-awake.svg)). Average spiking activity is maintained, only its temporal structure is reorganised, shifting from desynchronised to rhythmic activity. Therefore, the recording bouts displayed in [Fig.](../Figures/ephys-awake.svg) provide a clear illustration of the collective reorganisation of ongoing cortical activity as a function of behavioural states (see also [Poulet & Petersen, 2008](Poulet2008.pdf); [Niell & Stryker, 2010](Niell2010.pdf); [McGinley et al., 2015](McGinley2015a.pdf); [Vinck et al., 2015](Vinck2015); and see *section 2* of *Part \ref{part:past}* for a more detailed description of network activity during behavior). 

To summarise, our first example showed that intense mental effort corresponds to strong neural activity modulations but without a massive impact on its energetic cost, and our second example highlights how spiking activity is subtly temporally re-arranged across behavioural states while largely preserving firing rates.
Taken together, they illustrate that **the dynamic remodelling of neural activity is an essential working principle of brain function**. 
It is this principle, the fact that neural dynamics itself, and not merely activity levels, carries computational meaning, that motivates the strong emphasis I place on dynamics throughout my research.

On the other hand, the *functional consequences of such dynamic remodelling remain more elusive*. 

A natural hypothesis is that this interaction between *dynamics* and *computation* serves a specific functional role: **state-dependent modulations of neural dynamics provide the substrate through which cortical networks flexibly adapt their information-processing properties** to the animal's ongoing behavioural context, rather than applying a fixed, context-independent transformation of their inputs ([Ferguson & Cardin, 2020](Ferguson2020.pdf); [McCormick et al., 2020](McCormick2020.pdf); [Zerlaut & Tzilivaki, 2025](Zerlaut2025.pdf)).

Indeed, previous research has shown that those modulations of spiking dynamics are associated with alterations in the processing of incoming information.
For example, in mouse V1, the desynchronised cortical state accompanying locomotion strongly increases the gain of visually-evoked responses without altering the neurons' feature selectivity ([Niell & Stryker, 2010](Niell2010.pdf); [Reimer et al., 2014](Reimer2014.pdf); [Dadarlat & Stryker, 2017](Dadarlat2017.pdf)), thus suggesting a global improvement in sensory encoding, similar to the effect of attention in primate visual cortex ([Reynolds & Heeger, 2009](Reynolds2009.pdf)).
However, this relationship is not simply monotonic or uniform across sensory systems: in auditory cortex, comparable increases in arousal instead suppress sensory-evoked responses, and it is an intermediate (rather than maximal) arousal state that is associated with optimal discrimination of complex tones ([McGinley et al., 2015](McGinley2015a.pdf)). 
Such findings indicate that the functional consequence of state-dependent activity reorganisation is not a simple generic "gain increase," but a modality-, stimulus- and context-specific modulation of the input-output relationship of cortical circuits. 
A systematic, mechanistic account of this specificity as well as its circuit-level origins and computational logic is still largely lacking, thus remaining an important open question for the field.

It is therefore this question, the **interaction** between the *dynamical reorganization of neural activity* and the *information-processing properties* of cortical networks, that my research aims to describe and understand.
To tackle this, I combine both experimental and theoretical approaches in the laboratory.

On the theoretical side, I rely on numerical simulations and analytical descriptions of spiking network dynamics (see [Dayan & Abbott, 2001](Dayan2001.pdf); [Gerstner et al., 2014](Gerstner2014.pdf)), an approach central to the broader field of computational neuroscience ([Sejnowski et al., 1988](Sejnowski1988.pdf)).
This framework is particularly well suited to the analysis of dynamical modulations in cortical networks, as it makes it possible to incorporate key features of this phenomenon, such as *biophysical detail at the cellular level* (e.g., diverse receptor types, kinetics, morphology, synaptic interactions, adaptation dynamics, ...) as well as *circuit level features* (e.g., cell-type-specific connectivity, distinct excitatory and inhibitory subpopulations, specific wiring motifs, ...).
This approach thus makes it possible to relate the biophysical and circuit properties of cortical networks directly to the emergent, spike-based dynamics at the population level.

On the experimental side, the above-described arousal-dependent modulation of sensory cortex activity in the behaving rodent offers a particularly well-suited experimental model for studying this interaction.
First, sensory systems allow experimenters to precisely control inputs, making them well suited to characterising input-output transformations.
Second, the mouse model gives access to the modern neurophysiology toolkit that now makes it possible to observe such reorganisation at cellular resolution and on the timescale of single spikes. Combined with interventional approaches (genetic deletions, optogenetics, pharmacology, ...), this toolkit allows the circuits and mechanisms underlying specific computations to be dissected in detail ([Luo et al., 2018](Luo2018.pdf)).
Finally, and most importantly, cortical dynamics exhibit modulations of network activity (in terms of synchrony, low-frequency rhythms, ...) that appear to be general features of state-dependent modulation in the neocortex, seemingly conserved across species ([Harris & Thiele, 2011](Harris2011b.pdf)). 

Using those approaches, my previous work has mostly focused on the properties of the *dynamics* of cortical networks. In the *Past Research* (part \ref{part:past}), I review my previous work organised around the following sections:  

1. the study of the mechanisms and working principles of cellular integration in the network activity regimes characterising _in vivo_-like activity (see *Selected Publications \ref{sec:Zerlaut2016},\ref{sec:Zerlaut2017} & \ref{sec:Morabito2025}*)
2. the identification and modelling of the different network activity regimes displayed in sensory cortex during wakefulness (see *Selected Publications \ref{sec:Zerlaut2019} & \ref{sec:Zerlaut2022}*)
3. the dissection of the circuits, notably the interneuronal inhibitory networks, engaged in those modulations of network activity (see *Selected Publications \ref{sec:Morabito2025} & \ref{sec:VanVelze2024}*)
4. the integration of biophysical- and circuit-level features into large-scale models of cortical dynamics and cortical processing (see *Selected Publication \ref{sec:Zerlaut2018}*).

Now, my ongoing and future research aims at deepening this investigation by focusing on the **interaction** between _dynamics_ and _function_ in cortical networks. 
In the *Research Projects* (part \ref{part:projects}), I detail the different aspects of my current research programme structured around the following four sections:  

1. the study of the reconfiguration of cortical processing across behavioural states in the mouse visual cortex. 
2. the analysis of the circuit mechanisms of thalamo-cortical dynamics and its integration properties across the different states of wakefulness. 
3. the characterisation of the mechanisms behind the functional specificity of the different inhibitory populations of the mouse visual cortex.
4. the investigation of the modulation of cortical dynamics exerted by a particular sub-populations of inhibitory interneurons: the layer 1 NDNF+ interneurons.