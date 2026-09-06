# Dynamics of Thalamo-Cortical Networks during Wakefulness

In parallel to the previous experimental research axis, I will study the theoretical basis of flexible computation in neural networks, using both analytical approaches and numerical simulations. This problem can be summarised by the following question: how can the same neural network display different computational properties when modulated by a global input signal? This overarching question can be further broken down into three questions, which will structure my future research:

1. What are the different regimes of cortical activity resulting from the modulating input?
2. What is the relationship between dynamical regimes and computational properties?
3. What synaptic, cellular, and circuit properties allow the same neural network to display such flexibility?

Providing mechanistic insight into these questions will be the central theoretical focus of my future research. I detail the corresponding approach and methods below.

### Dynamical regimes of cortical activity during wakefulness

Because the change in computational properties occurs through the modulation of the regime of activity, a key prerequisite to this research is to capture as accurately as possible _the dynamical properties of the different regimes_ of the cortical networks observed in awake behaving animals.

While the anaesthetised cortex has been extensively analysed and modelled in the last 3 decades ([Compte et al., 2003](Compte2003.pdf); [Hill & Tononi, 2005](Hill2005.pdf); [Destexhe, 2009](Destexhe2009.pdf); reviewed in [Neske et al., 2016](Neske2016.pdf)), cortical physiology and sensory processing during active behaviour in rodents is a more recent topic ([Busse et al., 2017](Busse2017.pdf)). Much theoretical work remains to be done to account for the specificity of the dynamics of wakefulness. Indeed, depending on arousal and behavioural states, wakefulness corresponds to a non-trivial set of distinct activity regimes ([McGinley et al., 2015b](McGinley2015b.pdf); [Poulet & Petersen, 2019](Poulet2019.pdf); [Zerlaut et al., 2022](Zerlaut2022.pdf)), a mixture of oscillatory and asynchronous states (see [Fig.](../Figures/McGinley-2015.svg) in *Part \ref{part:past}*).
At low arousal levels ("drowsiness"), cortical activity tends to exhibit a stereotypical oscillation in the 3-6Hz delta-band range. At moderate arousal ("quiet" state), cortical activity is desynchronised, single cells are hyperpolarised and display low-amplitude membrane potential fluctuations. At high arousal levels ("active" state), activity is still desynchronised and the membrane potential exhibits sustained depolarisation with high firing activity and high-frequency fluctuations. **What are the minimal dynamical properties that enable the same neural assembly to display such a diversity of network states?** 

Importantly, recent evidence pinpoints the role of thalamo-cortical interactions in controlling the regimes of wakefulness ([Nestvogel & McCormick, 2022](Nestvogel2022.pdf)). A first step will thus be to design and implement a thalamo-cortical model reproducing the states of wakefulness. The thalamus indeed includes the biophysical components producing rhythmicity in recurrent networks ([Jahnsen & Llinás, 1984](Jahnsen1984.pdf); [van Krosigk et al., 1993](VonKrosigk1993.pdf)), so that, combined with a cortical model of the different asynchronous states in the cortical assembly ([Zerlaut et al., 2019](Zerlaut2019.pdf)), one can obtain a model reproducing all states of wakefulness.

I will perform this study using numerical simulations of recurrent networks of spiking neurons (in simplified models such as the Leaky Integrate-and-Fire ([Lapicque, 1907](Lapicque1907.pdf)) and AdExp ([Brette & Gerstner, 2005](Brette2005.pdf)) models) as well as using analytical approaches ([Renart et al., 2004](Renart2004.pdf)) to provide minimalistic dynamical descriptions of the activity regimes.


This model will serve as a theoretical foundation for much of the future work of the laboratory. Such a model will indeed provide a theoretical setting corresponding to the "control" condition of classical biological experiments. One can then mimic biological intervention by changing the model parameters (e.g. reducing quantal weight for the knockout of a synaptic receptor, decreasing membrane conductances for a pharmacological block, hyperpolarising for a photo-inactivation, etc...) and see if the emergent properties of the model explain the experimental observations. 

### Relationship between dynamical regimes and computational properties

The phenomenon at the core of this project is that the ongoing dynamics can affect the computation of input signals. While this phenomenon is a generic property of neural network models ([Nadim et al., 2008](Nadim2008.pdf)), _how this applies to the specific regimes of wakefulness remains unexplored_. I will therefore analyse how recurrent dynamics can modify the processing of incoming signals as a function of the network activity regime in the model derived with the above approach.

Importantly, the aim of this project is to characterise the "flexible computation" nature of neural network function. A simple characterisation based on a single metric for a single type of stimulus will not be able to capture such a property (see also I.1). It will not be able to demonstrate what is better performed in one state and what is better performed in the other state (only one can have a better performance). I will therefore work on custom metrics and custom stimulus paradigms to demonstrate the changes in signal processing and information transfer in the network. Here, I will build on my recently published approach to this question ([Zerlaut et al., 2019](Zerlaut2019.pdf), *Selected Publication \ref{sec:Zerlaut2019 }*).
I analysed the qualitative difference in computational properties in two different regimes of activity observed in the same network at different levels of modulatory activity. 
For the Afferent-Driven regime (AD, observed in the "quiet state" _in vivo_), I was able to demonstrate its high-encoding capability, using a neural pattern decoder of stimulus identity, when the network was stimulated with complex spatio-temporal patterns of presynaptic activity. For the Recurrent-Driven regime (RD, observed in the "active state" _in vivo_), I was able to demonstrate its high sensitivity, using a population-rate decoder of input strength. I will generalise this approach in my future work. I will explore how different input types (in terms of synaptic activity patterns that correspond to diverse statistics of visual stimuli, [Baudot et al., 2013](Baudot2013.pdf), see the experimental section) shape the spatio-temporal properties of evoked spiking patterns across the different states of recurrent dynamics.

### Circuit and biophysical properties underlying state-dependent processing


%%beginFigure%%
![](../Figures/scales-model.svg)
**| Modelling the complexity at different scales in excitatory/inhibitory (E/I) cortical networks.**
**(a)** Synaptic scale. Different properties of synaptic transmission, e.g. depression vs facilitation at E-to-I synapses (left) and AMPA vs AMPA+NMDA at excitatory synapses (right). 
**(b)** Cellular scale. Modelling cellular integration of synaptic input with cable theory: snapshot of the voltage profile along the dendritic tree. Adapted from [Morabito et al. (2022)](Morabito2022.pdf).
**(c)** Circuit scale. Schematic of the cortical network including the layer arrangement (I to VI) and some cell-type diversity (excitatory: Pyramidals and Stellate cells, molecularly-defined inhibitory neurons: PV, VIP, SST, NDNF).
%%endFigure%%


Neural networks are complex assemblies where complexity arises at all scales (see **[Fig.](../Figures/scales-model.svg)**), from synapses to cells to circuits. 
What are the system properties that critically shape the emergent phenomenon of state-dependent computation at the network level? 
In this part, I will leverage my expertise in biophysical and circuit modelling to address this question.

_1. At the synaptic level._ The rules of synaptic transmission greatly vary across the different pairs of presynaptic and postsynaptic cell types ([Fig.a](../Figures/scales-model.svg)). Synapses can either facilitate or depress to modulate signal transmission in the network. I will investigate whether such synaptic plasticity rules contribute to the state-dependence of network computations by varying the synaptic dynamics in the various connections of the network model. Synaptic dynamics can also vary due to the receptor involved in synaptic transmission. For example, excitatory (glutamatergic) synapses can either have a fast conductance time course (AMPA receptor) or slow voltage-dependent dynamics (NMDA receptor).

_2. At the cellular level._ Numerous cellular mechanisms are involved in the integration of synaptic inputs to shape the output spike pattern of a single cell. Active (voltage-dependent) conductances critically shape single-cell integration ([Koch, 2004](Koch2004.pdf)). Remarkably, their potential involvement in controlling the transition to and the maintenance of specific network states remains unexplored. Dendritic integration is also a complex phenomenon shaping single-cell computation ([Fig.b](../Figures/scales-model.svg); see [Morabito et al., 2025](Morabito2025.pdf) for their diversity across interneurons). 
Interestingly, recent work suggests non-trivial effects along the dendritic tree across different brain states ([Suzuki & Larkum, 2020](Suzuki2020.pdf); [Keijser & Sprekeler, 2022](Keijser2022.pdf)) (e.g. decoupling between the apical and basal arborisation). 
I will perform numerical simulations of biophysically and morphologically detailed cells while varying cellular parameters to analyse those questions.

_3. At the circuit level._ The interplay of excitatory and inhibitory populations arranged in recurrently connected networks can lead to complex and unintuitive phenomena. Making sense of the diversity of neuronal populations and their specific connectivity patterns is a significant challenge for neurophysiologists. First, the role of the layer organisation in the cortex is still largely unknown. I will thus analyse whether the sequential processing of signals across layers participates in state-dependent processing. Next, the diversity of interneurons in the cortex may be a key feature in orchestrating the different transitions and maintenance of the dynamically-diverse network states ([Zucca et al., 2017](Zucca2017.pdf)). I will therefore build and simulate multi-population models reproducing the circuit organisation of cortical assemblies ([Fig.c](../Figures/scales-model.svg)).

Using such a multi-scale modelling approach combined with the specific experimental characterisation of the previous section, I expect to reveal the essential features of cortical circuits that critically shape the emergence of state-dependent computation at the network level.



